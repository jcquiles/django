from django.db import models

# Create your models here.
# Describes the database objects used in the site.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')