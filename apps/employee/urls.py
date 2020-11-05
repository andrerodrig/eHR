from django.urls import path
from . import views as v

app_name = "employee"

urlpatterns = [
    path('', v.EmployeesList.as_view(), name='list_employees'),
    path('new/', v.EmployeeCreate.as_view(), name='create_employee'),
    path('edit/<int:pk>/', v.EmployeeEdit.as_view(), name='update_employee'),
    path('delete/<int:pk>/', v.EmployeeDelete.as_view(), name='delete_employee'),
    # URL for pdf geretation
    path('relatorio-funcionarios/', v.report_employees, name='report_employees'),
    path('exportar-csv/', v.ExportCSV.as_view(), name='export_csv'),
    path('exportar-excel/', v.ExportExcel.as_view(), name='export_excel'),

]
