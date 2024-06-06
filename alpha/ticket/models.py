from email.policy import default
from django.db import models

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField('TypeCategory')

    def __str__(self):
        return self.name

class TypeCategory(models.Model):
    type = models.ManyToManyField('Type')
    category = models.ManyToManyField('Category')

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name