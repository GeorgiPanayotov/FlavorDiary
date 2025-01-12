from django.db import models


class Ingredient(models.Model):
    ingredient_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    ingredient_picture = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )

    calories_per_hundred_grams = models.IntegerField(
        null=False,
        blank=False
    )

    price = models.IntegerField(

    )



