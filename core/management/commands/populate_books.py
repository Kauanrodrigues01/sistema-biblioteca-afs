from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Populate books'

    def handle(self, *args, **options):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        from bs4 import BeautifulSoup
        import time

        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Rodar em segundo plano
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        url = "https://rafalito92.github.io/bibliotecaafs/"
        driver.get(url)

        # Espera um tempo para o JavaScript carregar
        time.sleep(5)

        # Obtém o HTML atualizado
        page_source = driver.page_source

        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')

        books = soup.find_all('div', class_="book-card")

        for book in books:
            title = book.find('h2').text.strip()
            details = book.find_all("p")

            author = details[0].text.replace("Autor:", "").strip()
            isbn = details[1].text.replace("ISBN:", "").strip()
            publisher = details[2].text.replace("Editora:", "").strip()
            year = details[3].text.replace("Ano:", "").strip()
            genre = details[4].text.replace("Gênero:", "").strip()
            
            if not year.isnumeric():
                year = None
            
            if Book.objects.filter(isbn=isbn).exists():
                self.stdout.write(self.style.WARNING(f'Book {title} already exists, isbn: {isbn}!'))
                continue

            try:
                Book.objects.create(
                    title=title,
                    author=author,
                    isbn=isbn,
                    publisher=publisher,
                    year=year,
                    genre=genre
                )
                self.stdout.write(self.style.SUCCESS(f'Book {title} created successfully!'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating book {title}'))
                self.stdout.write(self.style.ERROR(f'{e}'))
