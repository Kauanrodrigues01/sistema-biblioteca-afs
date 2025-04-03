from django import forms
from books.models import Loan, Book
from django.utils import timezone


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['student', 'tier', 'book', 'loan_date', 'return_date']
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
