from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Department


class DepartmentList(ListView):
    model = Department

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        return Department.objects.filter(company=logged_company)


class DepartmentCreate(CreateView):
    model = Department
    fields = ['name']

    def form_valid(self, form):
        department = form.save(commit=False)
        department.company = self.request.user.employee.company
        department.save()
        return super(DepartmentCreate, self).form_valid(form)


class DepartmentEdit(UpdateView):
    model = Department
    fields = ['name']


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('department:list_departments')
