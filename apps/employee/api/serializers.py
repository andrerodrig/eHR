from apps.employee.models import Employee
from rest_framework import serializers
from apps.overtime.api.serializers import OvertimeRegisterSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    overtimeregister_set = OvertimeRegisterSerializer(many=True)

    class Meta:
        model = Employee
        fields = (
            'id', 'name',
            'department', 'user',
            'company', 'image',
            'total_overtime', 'overtimeregister_set',
        )
