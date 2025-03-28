from django.contrib import admin
from .models import Book, Loan

# books/admin.py
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'get_turma_display', 'livro', 'data_emprestimo', 'data_devolucao')
    list_filter = ('turma', 'data_emprestimo')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = 'title',