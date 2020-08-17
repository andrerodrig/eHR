from django.db import models
from django.urls import reverse

from apps.employee.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Employee, on_delete=models.PROTECT)
    file = models.FileField(upload_to='documents')

    def get_absolute_url(self):
        return reverse("employee:update_employee", args=[self.owner.id])

    def __str__(self):
        return self.description
