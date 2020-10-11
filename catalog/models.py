from django.db import models

# Create your models here.

from django.urls import reverse
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(max_length=1000, help_text="Небольшое описание книги")
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр книги")
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3]])
        display_genre.short_description = 'Genre'

