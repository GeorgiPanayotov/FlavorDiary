from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    MAX_NAME_LENGTH = 20

    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    phone_number = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        # validators=[RegexValidator(r'^\+?\d+$', 'Enter a valid phone number.')]
    )

    address = models.TextField(
        blank=True
    )

