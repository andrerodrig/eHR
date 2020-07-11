"""Model for employee"""
from django.db import models
from django.contrib.auth.models import User
from apps.department.models import Department
from apps.company.models import Company


class Employee(models.Model):
    """ORM class for Employee"""

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ManyToManyField(Department)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
