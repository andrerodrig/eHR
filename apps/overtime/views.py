import json
import io
import csv
import xlwt

from reportlab.pdfgen import canvas

from django.http import FileResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    TemplateView,
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

        response = json.dumps({
            'mensagem': 'Hora extra marcada como utilizada.',
            'horas': float(employee.total_overtime)
        })

        return HttpResponse(response, content_type='application/json')


class HasNotUsedOvertime(View):

    def post(self, *args, **kwargs):
        overtime_register = OvertimeRegister.objects.get(pk=kwargs['pk'])
        overtime_register.used = False
        overtime_register.save()

        employee = self.request.user.employee

        response = json.dumps({
            'mensagem': 'Hora extra marcada como não utilizada',
            'horas': float(employee.total_overtime)
        })

        return HttpResponse(response, content_type='application/json')


class ExportCSV(View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=somefile.csv'

        bd_hours_regist = OvertimeRegister.objects.filter(used=False)

        writer = csv.writer(response)
        writer.writerow(['ID', 'Motivo', 'Funcionario',
                         'Horas', 'Horas Restantes'])

        for item in bd_hours_regist:
            writer.writerow(
                [item.id,
                 item.reason,
                 item.employee,
                 item.hours,
                 item.employee.total_overtime])

        return response


class ExportExcel(View):

    def get(self, request):
        response = HttpResponse(content_type='text/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        columns = ['ID', 'Motivo', 'Funcionario', 'Horas', 'Horas Restantes']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        h_regist = OvertimeRegister.objects.filter(used=False)

        row_num = 1
        for regist in h_regist:
            # breakpoint()
            ws.write(row_num, 0, regist.id)
            ws.write(row_num, 1, regist.reason)
            ws.write(row_num, 2, regist.employee.name)
            ws.write(row_num, 3, regist.hours)
            ws.write(row_num, 4, regist.employee.total_overtime)

            row_num += 1

        wb.save(response)
        return response


def report_overtime_database(request):
    # Create the Buffer
    buffer = io.BytesIO()
    # Generating the pdf object for the buffer
    p = canvas.Canvas(buffer)
    overtime_db = OvertimeRegister.objects.all()
    str_data = 'Motivo: %s | Funcionário: %s | Horas: %.2f'
    y = 780
    p.drawString(10, 800, 'Banco de Horas')
    for overtime in overtime_db:
        p.drawString(10, y, str_data %
                     (overtime.reason, overtime.employee, overtime.hours))
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='relatorio-banco-de-horas.pdf')
