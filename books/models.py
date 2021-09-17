from django.db import models
from django.db.models.query import QuerySet

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField('date published')
    quantity = models.IntegerField(default=0)
