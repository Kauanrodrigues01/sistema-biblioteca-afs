from django.contrib import admin
from .models import Book, Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'get_tier_display', 'book', 'loan_date', 'return_date')
    list_filter = ('tier', 'loan_date')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'author', 'publisher', 'year', 'genre')
