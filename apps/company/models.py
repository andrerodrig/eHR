from django.db import models
from django.shortcuts import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the Company')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:home")
