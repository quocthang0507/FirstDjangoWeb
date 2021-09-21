import books
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Book
# Create your views here.


# def index(request):
#     latest_book_list = Book.objects.order_by('-published_date')[:5]
#     template = loader.get_template('books/index.html')
#     context = {'latest_book_list': latest_book_list}
#     return HttpResponse(template.render(context, request))


# shortcut
def index(request):
    latest_book_list = Book.objects.order_by('-published_date')[:5]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/index.html', context)


# def detail(request, book_id):
#     try:
#         book = Book.objects.get(pk=book_id)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist!')
#     return render(request, 'books/detail.html', {'book': book})

# shortcut
def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})


def table_content(request, book_id):
    return HttpResponse('You\'re looking at table of content %s.' % book_id)


def read(request, book_id):
    return HttpResponse('You\'re reading book %s.' % book_id)
