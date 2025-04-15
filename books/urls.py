from django.urls import path
from .views import login_view, create_loan, list_loan, logout, delete_loan, home, create_book



urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('emprestimos/criar/', create_loan, name='create_loan'),
    path('criar/livro', create_book, name='create_book'),
    path('emprestimos', list_loan, name='list_loan'),
    path('emprestimo/deletar/<int:emprestimo_id>/', delete_loan, name='delete_loan'),
]