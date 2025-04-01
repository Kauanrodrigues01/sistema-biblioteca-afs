from django import forms
from books.models import Loan, Book
from django.utils import timezone



class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['aluno', 'turma', 'livro', 'editora', 'data_emprestimo', 'data_devolucao']
        widgets = {
            'data_emprestimo': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': timezone.now().date().strftime('%Y-%m-%d')
            }),
            'data_devolucao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': timezone.now().date().strftime('%Y-%m-%d')
            }),
            'aluno': forms.TextInput(attrs={'class': 'form-control'}),
            'turma': forms.Select(attrs={'class': 'form-control'}),
            'livro': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'aluno': 'Aluno(a)',
            'turma': 'Turma',
            'livro': 'Livro',
            'editora': 'Editora',
            'data_emprestimo': 'Data de Emprestimo',
            'data_devolucao': 'Data de Devolução'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['livro'].queryset = Book.objects.all().filter(available=True)
