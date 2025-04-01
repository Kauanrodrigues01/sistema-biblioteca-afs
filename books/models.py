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
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.title

class Loan(models.Model):
    TURMAS_CHOICES = [
        # Desenvolvimento de Sistemas
        ('1DS', '1º Desenvolvimento de Sistemas'),
        ('2DS', '2º Desenvolvimento de Sistemas'),
        ('3DS', '3º Desenvolvimento de Sistemas'),

        # Administração
        ('1A', '1º Administração'),
        ('2A', '2º Administração'),
        ('3A', '3º Administração'),
        
        # Enfermagem
        ('1E', '1º Enfermagem'),
        ('2E', '2º Enfermagem'),
        ('3E', '3º Enfermagem'),
        
        # Informática
        ('1I', '1º Informática'),
        ('2I', '2º Informática'),
        ('3I', '3º Informática'),
        
        # Logística
        ('1L', '1º Logística'),
        ('2L', '2º Logística'),
        ('3L', '3º Logística'),
    ]
    aluno = models.CharField(max_length=100, verbose_name='Aluno(a)')
    turma =models.CharField(max_length=100, choices=TURMAS_CHOICES, verbose_name='Turma')
    livro = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Livro')
    data_emprestimo = models.DateField(default=timezone.now, verbose_name='Data de Empréstimo')
    data_devolucao = models.DateField(verbose_name='Data de Devolução')
    devolvido = models.BooleanField(default=False, verbose_name='Devolvivo?')
    editora = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['data_emprestimo']
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    @property
    def esta_atrasado(self):
        if self.devolvido:
            return False
        elif timezone.now().date() > self.data_devolucao:
            return True
        return False
            
    def __str__(self):
        return f"{self.aluno} - {self.livro.title}"
