from rest_framework import viewsets
from apps.employee.api.serializers import EmployeeSerializer
from apps.employee.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
