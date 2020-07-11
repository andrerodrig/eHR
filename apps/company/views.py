from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Company


class CompanyCreate(CreateView):
    model = Company
    fields = ["name"]

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employee
        employee.company = obj
        employee.save()
        return HttpResponse('Ok')


class CompanyEdit(UpdateView):
    model = Company
    fields = ["name"]
