from django.contrib import admin

from . import models

# Register your models here.
from .models import Book
admin.site.register(Book)