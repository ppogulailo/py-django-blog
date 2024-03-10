from django.db.models import Avg
from django.http import Http404
from django.shortcuts import get_object_or_404,render

from .models import Book


# Create your views here.

def index(req):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))['rating__avg']
    return render(req, 'book_outlet/index.html', {
        "books": books,
        "total_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(req, slug):
    # try:
    #     books = Book.objects.get(pk=id)
    # except:
    #     raise Http404("Book not found")
    books = get_object_or_404(Book,slug=slug)
    return render(req, 'book_outlet/book_detail.html', {
        "title": books.title,
        "author": books.author,
        "rating": books.rating,
        "slug":books.slug,
        "is_bestseller": books.is_bestselling
    })
