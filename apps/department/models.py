"""Models for Department"""
from django.db import models


class Department(models.Model):
    """ORM class for Department"""

    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
