from django.contrib import admin
from FlavorDiary.ingredients.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'price')
    search_fields = ('ingredient_name', 'price')
