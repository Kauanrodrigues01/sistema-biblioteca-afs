from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Book, Loan
from books.forms import LoanForm, CreateBook
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse


def home(request):
    livros = Book.objects.order_by('title')
    return render(request, 'books/home.html', {'books': livros})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('create_loan')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso.')
            return redirect('create_loan')

        error = 'Credenciais inválidas'
        messages.error(request, error)
        return render(request, 'books/login.html', {'error': error})
    return render(request, 'books/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')


@login_required
def create_loan(request):
    hoje = timezone.now().date()

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']

            # Verifica se livro já está emprestado
            if not book.available:
                messages.error(request, 'Este livro já está emprestado!')
                return redirect('create_loan')

            # Atualiza status do livro
            book.available = False
            book.save()

            # Cria empréstimo
            form.save()

            messages.success(request, "Empréstimo criado com sucesso")
            return redirect('create_loan')
    else:
        form = LoanForm(initial={'loan_date': hoje})

    # Recupera empréstimos para a lista
    emprestimos = Loan.objects.all().order_by('-loan_date')

    return render(request, 'books/loan_form.html', {
        'form': form,
        'emprestimos': emprestimos,
        'hoje': hoje
    })


@login_required
def delete_loan(request, emprestimo_id):
    emprestimo = get_object_or_404(Loan, id=emprestimo_id)

    # Libera o livro antes de deletar
    book = emprestimo.book
    book.available = True
    book.save()

    # Deleta o empréstimo
    emprestimo.delete()

    messages.success(request, 'Empréstimo removido com sucesso!')
    return redirect('create_loan')  # Redireciona para a página de cadastro


@login_required
def create_book(request):
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect(reverse('create_loan') + f'?book_id={book.id}')
        return render(request, 'books/create.html', {'form': form})

    form = CreateBook()
    return render(request, 'books/create_book.html', {'form': form})
