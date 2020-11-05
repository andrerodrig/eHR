from django.urls import path

from . import views as v

app_name = 'department'

urlpatterns = [
    path('', v.DepartmentList.as_view(), name='list_departments'),
    path('new/', v.DepartmentCreate.as_view(), name='create_department'),
    path('edit/<int:pk>/',
         v.DepartmentEdit.as_view(),
         name='update_department'
         ),
    path('delete/<int:pk>/', v.DepartmentDelete.as_view(),
         name='delete_department'
         ),
    path('report-departments/', v.report_departments, name='report_departments'),
    path('exportar-csv/', v.ExportCSV.as_view(), name='export_csv'),
    path('exportar-excel/', v.ExportExcel.as_view(), name='export_excel'),
]
