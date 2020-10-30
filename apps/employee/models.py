"""Model for employee"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum

from apps.department.models import Department
from apps.company.models import Company


class Employee(models.Model):
    """ORM class for Employee"""

    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ManyToManyField(Department)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total_overtime(self):
        total = self.overtimeregister_set.all().aggregate(
            Sum('hours'))['hours__sum']

        return total

    def get_absolute_url(self):
        return reverse("employee:list_employees")

    def __str__(self):
        return self.name
