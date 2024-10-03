from django.contrib import admin
from .models import Breed, Cat, Rating


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'color', 'age', 'description', 'owner'
    )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'cat', 'rate'
    )
