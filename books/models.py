from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200, null=True)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Loan(models.Model):
    TIERS = (
        ('1D', '1º Desenvolvimento de Sistemas'),
        ('2D', '2º Desenvolvimento de Sistemas'),
        ('3D', '3º Desenvolvimento de Sistemas'),
        ('1E', '1º Enfermagem'),
        ('2E', '2º Enfermagem'),
        ('3E', '3º Enfermagem'),
        ('1A', '1º Administração'),
        ('2A', '2º Administração'),
        ('3A', '3º Administração'),
        ('1L', '1º Logística'),
        ('2L', '2º Logística'),
        ('3L', '3º Logística'),
        ('1I', '1º Informática'),
        ('2I', '2º Informática'),
        ('3I', '3º Informática'),
    )
    student_name = models.CharField(max_length=100)
    tier = models.CharField(max_length=100, choices=TIERS)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f'{self.book} - {self.student_name}'
