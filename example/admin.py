from django.contrib import admin

# Register your models here.

from .models import Review, Recipe

admin.site.register(Review)
admin.site.register(Recipe)