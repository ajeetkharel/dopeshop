from django.contrib import admin
from .models import Item
from users.models import Category, Owner

admin.site.register(Item)
admin.site.register(Category)