from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Book, Genre

def index(request):
    num_books = Book.objects.all().count()

    return render(request, 'index.html', context={'num_books':num_books})

class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'my_book_list'
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book