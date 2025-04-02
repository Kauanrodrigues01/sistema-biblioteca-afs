# Generated by Django 5.1.7 on 2025-04-02 02:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('isbn', models.CharField(max_length=13)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=100, verbose_name='Aluno(a)')),
                ('tier', models.CharField(choices=[('1DS', '1º Desenvolvimento de Sistemas'), ('2DS', '2º Desenvolvimento de Sistemas'), ('3DS', '3º Desenvolvimento de Sistemas'), ('1A', '1º Administração'), ('2A', '2º Administração'), ('3A', '3º Administração'), ('1E', '1º Enfermagem'), ('2E', '2º Enfermagem'), ('3E', '3º Enfermagem'), ('1I', '1º Informática'), ('2I', '2º Informática'), ('3I', '3º Informática'), ('1L', '1º Logística'), ('2L', '2º Logística'), ('3L', '3º Logística')], max_length=100, verbose_name='Turma')),
                ('loan_date', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Empréstimo')),
                ('return_date', models.DateField(verbose_name='Data de Devolução')),
                ('returned', models.BooleanField(default=False, verbose_name='Devolvivo?')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Livro')),
            ],
            options={
                'verbose_name': 'Empréstimo',
                'verbose_name_plural': 'Empréstimos',
                'ordering': ['loan_date'],
            },
        ),
    ]
