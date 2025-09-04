from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # This ends the user session
    return redirect('login')  # Redirect to login page or any other page

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

