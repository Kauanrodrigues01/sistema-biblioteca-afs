from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Populate books'

    def handle(self, *args, **options):
        import json

        with open('./books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for book in data:
                if not book['year'].isnumeric():
                    book['year'] = None
                
                book_author_lower = book['author'].lower()
                if book_author_lower == 'autor desconhecido' or book_author_lower == 'author unknown' or book_author_lower == 'author unknown' or book_author_lower == 'null':
                    book['author'] == None

                book_publisher_lower = book['publisher'].lower()
                if book_publisher_lower == 'null' or book_publisher_lower == 'editora não especificada':
                    book['publisher'] == None

                try:
                    Book.objects.create(
                        title=book['title'],
                        author=book['author'],
                        isbn=book['isbn'],
                        publisher=book['publisher'],
                        year=book['year'],
                        genre=book['genre'],
                    )
                    self.stdout.write(self.style.SUCCESS(f'Book "{book["title"]}" created successfully.'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error: {e}'))
