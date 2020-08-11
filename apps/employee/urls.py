from django.urls import path
from . import views as v

app_name = "employee"

urlpatterns = [
    path('', v.EmployeesList.as_view(), name='list_employees'),
    path('new', v.EmployeeNew.as_view(), name='create_employee'),
    path('edit/<int:pk>', v.EmployeeEdit.as_view(), name='update_employee'),
    path('delete/<int:pk>', v.EmployeeDelete.as_view(), name='delete_employee'),
]
