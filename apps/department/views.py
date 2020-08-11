from django.shortcuts import render
from django.views.generic import ListView

from .models import Department


class DepartmentList(ListView):
    model = Department

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        return Department.objects.filter(company=logged_company)
