from django.contrib import admin
from .models import System, Type, Category, TypeCategory

# Register your models here.
admin.site.register(System)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(TypeCategory)