from django.db import models


class OvertimeRegister(models.Model):
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.reason
