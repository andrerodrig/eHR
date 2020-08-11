from django.urls import path

from . import views as v

app_name = 'department'

urlpatterns = [
    path('', v.DepartmentList.as_view(), name='list_departments'),
]
