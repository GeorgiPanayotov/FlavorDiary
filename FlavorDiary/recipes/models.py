from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(
        max_length=100,
    )

    ingredients = models.ManyToManyField(
        to='ingredients.Ingredient',
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

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name
