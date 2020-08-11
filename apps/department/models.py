"""Models for Department"""
from django.db import models
from apps.company.models import Company


class Department(models.Model):
    """ORM class for Department"""

    name = models.CharField(max_length=70)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
