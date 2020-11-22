from celery import shared_task
from apps.employee.models import Employee
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_report():
    total = Employee.objects.all().count()
    send_mail(
        'Report Celery',
        'General Report for employees: %f' % total,
        'andrelmarques11@gmail.com',
        ['mrodriguesandr@gmail.com'],
        fail_silently=False,
    )

    return True
