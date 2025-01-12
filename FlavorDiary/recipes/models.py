from django.db import models
from FlavorDiary.ingredients.models import Ingredient


class Recipe(models.Model):
    recipe_name = models.CharField(
        max_length=100,
    )

    ingredients = models.ManyToManyField(
        'Ingredient',
        related_name='recipes',
        through='IngredientRecipe'
    )

    ingredient_quantity = models.IntegerField(
        default=0,
    )

    cooking_time = models.IntegerField(
        default=0,
        blank=True,
    )

    def __str__(self):
        return self.recipe_name
