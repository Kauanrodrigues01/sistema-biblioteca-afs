from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200, null=True)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    genre = models.CharField(max_length=100, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Loan(models.Model):
    TURMAS_CHOICES = [
        ('1A', '1º ADMNISTRAÇÃO'),
        ('1E', '1º ENFERMAGEM'),
        ('1I', '1º INFORMÁTICA'),
        ('1L', '1º LOGISCA'),
        ('2A', '2º ADMNISTRÇÃO'),
        ('2E', '2º ENFERMAGEM'),
        ('2DS','2º DESENVOLVIMENTO'),
        ('2L', '2º LOGISCA'),
        ('3A', '3º ADMNISTRAÇÃO'),
        ('3E', '3º ENFERMAGEM'),
        ('3DS', '3º DESENVOLVIMENTO'),
        ('3I', '3º INFORMATICA'),
    ]
    aluno = models.CharField(max_length=100, verbose_name='Aluno(a)')
    turma =models.CharField(max_length=100, choices=TURMAS_CHOICES, verbose_name='Turma')
    livro = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Livro')
    data_emprestimo = models.DateField(default=timezone.now, verbose_name='Data de Empréstimo')
    data_devolucao = models.DateField(verbose_name='Data de Devolução')
    devolvido = models.BooleanField(default=False, verbose_name='Devolvivo?')
    editora = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['data_devolucao']
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    def status(self):
        if self.devolvido:
            return "Devolvido"
        elif timezone.now().date() > self.data_devolucao:
            return "Atrasado"
        return "Em dia"
            
    def __str__(self):
        return f"{self.aluno} - {self.livro.title}"