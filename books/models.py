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
