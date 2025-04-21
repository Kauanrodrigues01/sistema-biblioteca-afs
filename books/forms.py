from django import forms
from books.models import Loan, Book
from django.utils import timezone
from datetime import datetime
from datetime import date, timedelta


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'student', 'tier', 'loan_date', 'return_date']
        widgets = {
            'loan_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': timezone.now().date().strftime('%Y-%m-%d')
            }),
            'return_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': timezone.now().date().strftime('%Y-%m-%d')
            }),
            'student': forms.TextInput(attrs={'class': 'form-control'}),
            'tier': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'student': 'Aluno(a)',
            'tier': 'Turma',
            'book': 'Livro',
            'loan_date': 'Data de Emprestimo',
            'return_date': 'Data de Devolução'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all().filter(available=True)

        today = date.today()
        self.fields['loan_date'].initial = today
        self.fields['return_date'].initial = today + timedelta(days=14)

        if 'readonly' in self.fields['loan_date'].widget.attrs:
            del self.fields['loan_date'].widget.attrs['readonly']
        if 'readonly' in self.fields['return_date'].widget.attrs:
            del self.fields['return_date'].widget.attrs['readonly']


class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publisher', 'year', 'genre']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'isbn': 'ISBN',
            'publisher': 'Editora',
            'year': 'Ano de Publicação',
            'genre': 'Gênero',
        }
        widgets = {
            'year': forms.NumberInput(attrs={
                'min': 1000,
                'max': datetime.now().year + 1
            }),
        }

        def clean_isbn(self):
            isbn = self.cleaned_data.get('isbn')
            if len(isbn) not in [10, 13] or not isbn.isdigit():
                raise forms.ValidationError("ISBN deve conter 10 ou 13 dígitos numéricos.")
            return isbn
