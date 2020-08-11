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
]
