from django.contrib import admin
from .models import Category, Figure, Review, UserPreference

admin.site.register(Category)
admin.site.register(Figure)
admin.site.register(Review)
admin.site.register(UserPreference)