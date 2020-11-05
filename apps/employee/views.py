import io
import csv
import xlwt

from reportlab.pdfgen import canvas

from django.http import FileResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    View,
)

from .models import Employee


class EmployeesList(ListView):
    model = Employee

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        return Employee.objects.filter(company=logged_company)


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'department']

    def form_valid(self, form):
        employee = form.save(commit=False)
        username = employee.name.split(' ')[0] + employee.name.split(' ')[1]
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(EmployeeCreate, self).form_valid(form)


class EmployeeEdit(UpdateView):
    model = Employee
    fields = ['name', 'department']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee:list_employees')


class ExportCSV(View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio-funcionarios.csv"'

        employees = Employee.objects.filter(
            company=request.user.employee.company)
        writer = csv.writer(response)
        writer.writerow(['Usuario', 'Nome', 'Email', 'Banco de Horas'])

        for e in employees:
            writer.writerow([
                e.user.username,
                e.name,
                e.user.email,
                e.total_overtime,
            ])

        return response


class ExportExcel(View):

    def get(self, request):
        response = HttpResponse(content_type='text/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Funcionários')

        row_num = 0

        columns = ['Usuário', 'Nome', 'Email', 'Banco de Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        employees = Employee.objects.filter(
            company=request.user.employee.company)

        row_num = 1
        for e in employees:
            # breakpoint()
            ws.write(row_num, 0, e.user.username)
            ws.write(row_num, 1, e.name)
            ws.write(row_num, 2, e.user.email)
            ws.write(row_num, 3, e.total_overtime)

            row_num += 1

        wb.save(response)
        return response


def report_employees(request):
    # Creating a file-like buffer to receive the pdf data
    buffer = io.BytesIO()

    # Creating a pdf object, using the buffer as it file
    p = canvas.Canvas(buffer)

    employees = Employee.objects.all()

    str_data = 'Nome: %s | Hora Extra: %.2f'

    y = 790
    for employee in employees:
        p.drawString(10, y, str_data % (
            employee.name, employee.total_overtime))
        y -= 40

    # Close the PDF cleanly, and we're done
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
