from django.contrib.auth.models import AbstractUser
from django.db import models
# from cloudinary.models import CloudinaryField


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

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        # validators=[NameValidator()], """NameValidator to be added"""
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        # validators=[NameValidator()], """NameValidator to be added"""
        blank=False,
        null=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    # profile_picture = CloudinaryField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Profile Picture',
    # )

    bio = models.TextField(
        blank=True
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

