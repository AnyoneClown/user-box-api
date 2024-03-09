from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    class LangaugeChoices(models.TextChoices):
        ENGLISH = "English"
        UKRAINIAN = "Ukrainian"
        FRENCH = "French"

    class CountyChoices(models.TextChoices):
        USA = "USA"
        UKRAINE = "Ukraine"
        FRANCE = "France"

    telegram_id = models.IntegerField(max_length=20, unique=True)
    telegram_username = models.CharField(max_length=50, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    language = models.CharField(choices=LangaugeChoices.choices, max_length=50)
    country = models.CharField(choices=CountyChoices.choices, max_length=50)
    verification_code = models.CharField(max_length=6)

    class Meta:
        ordering = ["telegram_username"]
        verbose_name = "User"
        verbose_name_plural = "Users"
        app_label = "user"
        db_table = "users"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"User: {self.telegram_username}"
