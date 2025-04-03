from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200, null=True, blank=True)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.title

class Loan(models.Model):
    TIERS = [
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
    student = models.CharField(max_length=100, verbose_name='Aluno(a)')
    tier =models.CharField(max_length=100, choices=TIERS, verbose_name='Turma')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Livro')
    loan_date = models.DateField(default=timezone.now, verbose_name='Data de Empréstimo')
    return_date = models.DateField(verbose_name='Data de Devolução')
    returned = models.BooleanField(default=False, verbose_name='Devolvivo?')
    class Meta:
        ordering = ['loan_date']
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    @property
    def is_late(self):
        if self.returned:  # Already returned → "on_time"
            return "on_time"
        
        today = timezone.now().date()
        
        if today > self.return_date:  # Past due → "late"
            return "late"
        elif today == self.return_date:  # Due today → "warning"
            return "warning"
        else:  # Future due date → "on_time"
            return "on_time"
            
    def __str__(self):
        return f"{self.student} - {self.book.title}"
