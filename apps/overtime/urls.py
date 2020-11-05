from django.urls import path

from . import views as v

app_name = 'overtime'

urlpatterns = [
    path('', v.OvertimeList.as_view(), name='list_overtime'),
    path('new/', v.OvertimeCreate.as_view(), name='create_overtime'),
    path('edit-funcionario/<int:pk>',
         v.OvertimeEdit.as_view(), name='update_overtime'),
    path('edit/<int:pk>', v.OvertimeBaseEdit.as_view(),
         name='update_overtime_base'),
    path('utilizou-hora-extra/<int:pk>', v.HasUsedOvertime.as_view(),
         name='utilizou_hora_extra'),
    path('nao-utilizou-hora-extra/<int:pk>', v.HasNotUsedOvertime.as_view(),
         name='nao_utilizou_hora_extra'),
    path('relatorio-bd-horas/', v.report_overtime_database,
         name='report_overtime'),
    path('export-csv/', v.ExportCSV.as_view(),
         name='export_csv'),
    path('export-excel/', v.ExportExcel.as_view(),
         name='export_excel'),
    path('delete/<int:pk>', v.OvertimeDelete.as_view(), name='delete_overtime'),
]
