from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tag, Category, Article

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
