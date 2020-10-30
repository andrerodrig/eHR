import json
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)

from .models import OvertimeRegister
from .forms import OvertimeRegisterForm


class OvertimeList(ListView):
    model = OvertimeRegister

    def get_queryset(self):
        """Filter only overtimes from the logged company"""
        logged_company = self.request.user.employee.company
        return OvertimeRegister.objects.filter(employee__company=logged_company)


class OvertimeEdit(UpdateView):
    model = OvertimeRegister
    form_class = OvertimeRegisterForm

    def get_form_kwargs(self):
        kwargs = super(OvertimeEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OvertimeBaseEdit(UpdateView):
    model = OvertimeRegister
    form_class = OvertimeRegisterForm
    success_url = reverse_lazy('overtime:list_overtime')

    def get_form_kwargs(self):
        kwargs = super(OvertimeBaseEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class OvertimeDelete(DeleteView):
    model = OvertimeRegister
    success_url = reverse_lazy('overtime:list_overtime')


class OvertimeCreate(CreateView):
    model = OvertimeRegister
    form_class = OvertimeRegisterForm
    success_url = reverse_lazy('overtime:list_overtime')

    def get_form_kwargs(self):
        kwargs = super(OvertimeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HasUsedOvertime(View):

    def post(self, *args, **kwargs):
        overtime_register = OvertimeRegister.objects.get(pk=kwargs['pk'])
        overtime_register.used = True
        overtime_register.save()

        employee = self.request.user.employee
        print(employee.total_overtime)

        response = json.dumps({
            'mensagem': 'Hora extra marcada como utilizada.',
            'horas': float(employee.total_overtime)
        })

        return HttpResponse(response, content_type='application/json')
