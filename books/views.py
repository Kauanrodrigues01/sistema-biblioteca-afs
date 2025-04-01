from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Book, Loan
from books.forms import LoanForm
from django.contrib import messages
from django.utils import timezone

from django.shortcuts import render
from .models import Book

def home(request):
    livros = Book.objects.filter(available=True).order_by('title')
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
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('create_loan')
        error = 'Credenciais inválidas'
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': error})
        return render(request, 'books/login.html', {'error': error})
    return render(request, 'books/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

@login_required
def create_loan(request):
    messages.success(request, 'Testando a mensagem')
    hoje = timezone.now().date()
    
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            livro = form.cleaned_data['livro']
            
            # Verifica se livro já está emprestado
            if not livro.available:
                messages.error(request, 'Este livro já está emprestado!')
                return redirect('create_loan')
                
            # Atualiza status do livro
            livro.available = False
            livro.save()
            
            # Cria empréstimo
            form.save()
            
            messages.success(request, "Empréstimo criado com sucesso")
            return redirect('create_loan')
    else:
        form = LoanForm(initial={'data_emprestimo': hoje})

    # Recupera empréstimos para a lista
    emprestimos = Loan.objects.all().order_by('-data_emprestimo')
    
    return render(request, 'books/loan_form.html', {
        'form': form,
        'emprestimos': emprestimos,
        'hoje': hoje
    })

@login_required
def list_loan(request):
    emprestimos = Loan.objects.all().order_by('-data_emprestimo').select_related('livro')

    context = {
        'emprestimos': emprestimos,
        'turmas_choices': Loan.TURMAS_CHOICES,
        'livros': Book.objects.all(),
        'timezone': timezone
    }
    return render(request, 'books/loan_list.html', context)

@login_required
def delete_loan(request, emprestimo_id):
    emprestimo = get_object_or_404(Loan, id=emprestimo_id)
    
    # Libera o livro antes de deletar
    livro = emprestimo.livro
    livro.disponivel = True
    livro.save()
    
    # Deleta o empréstimo
    emprestimo.delete()
    
    messages.success(request, 'Empréstimo removido com sucesso!')
    return redirect('create_loan')  # Redireciona para a página de cadastro