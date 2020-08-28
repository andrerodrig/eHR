from django.db import models
from django.urls import reverse

from apps.employee.models import Employee


class OvertimeRegister(models.Model):
    reason = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse("overtime:update_overtime", kwargs={"pk": self.pk})

    def __str__(self):
        return self.reason
