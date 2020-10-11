from django.contrib import admin

# Register your models here.
from .models import Genre, Book

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class BooksInline(admin.StackedInline):
    model = Book
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre')


