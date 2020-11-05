import io
import csv
import xlwt

from reportlab.pdfgen import canvas

from django.http import FileResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
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


class ExportCSV(View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio-departamentos.csv"'

        departments = Department.objects.filter(
            company=request.user.employee.company
        )

        writer = csv.writer(response)
        writer.writerow(['ID', 'Nome'])

        for d in departments:
            writer.writerow([
                d.id,
                d.name,
            ])

        return response


class ExportExcel(View):

    def get(self, request):
        response = HttpResponse(content_type='text/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Departamentos')

        row_num = 0

        columns = ['ID', 'Nome']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        departments = Department.objects.filter(
            company=request.user.employee.company)

        row_num = 1
        for d in departments:
            # breakpoint()
            ws.write(row_num, 0, d.id)
            ws.write(row_num, 1, d.name)

            row_num += 1

        wb.save(response)
        return response


def report_departments(request):
    # Create the buffer
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    departments = Department.objects.all()

    str_data = 'Departamento: %s'

    y = 780

    p.drawString(
        10,
        800,
        'Departamentos - %s' % (request.user.employee.company)
    )

    for department in departments:
        p.drawString(10, y, str_data % (department.name))
        y -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(
        buffer,
        as_attachment=True,
        filename='Relatorio - Departamentos.pdf'
    )
