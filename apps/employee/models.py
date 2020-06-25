"""Model for employee"""
from django.db import models


class Employee(models.Model):
    """ORM class for Employee"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
