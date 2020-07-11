from django.db import models
from apps.employee.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.description
