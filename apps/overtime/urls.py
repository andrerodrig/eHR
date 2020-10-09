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
    path('delete/<int:pk>', v.OvertimeDelete.as_view(), name='delete_overtime'),
]
