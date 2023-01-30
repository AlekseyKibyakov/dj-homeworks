from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book

def convert_date(books):
    for book in books:
        book.pub_date = str(book.pub_date)
    return books



def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    convert_date(books)
    context = {'books': books}
    return render(request, template, context)

def one_book_view(request, date):
    template = 'books/date_list.html'
    books = Book.objects.filter(pub_date__contains=date)
    paginator = Paginator(books, 10)
    page_date = request.GET.get('pub_date')
    page = paginator.get_page(page_date)
    prev_date = Book.objects.filter(pub_date__lt=date).values('pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=date).values('pub_date').first()

    if prev_date:
        prev_date = str(prev_date['pub_date'])
    
    if next_date:
        next_date = str(next_date['pub_date'])

    context = {
        'books': books,
        'page': page,
        'prev_date': prev_date,
        'next_date': next_date,
        }
    return render(request, template, context)
