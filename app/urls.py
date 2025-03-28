from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
] 
