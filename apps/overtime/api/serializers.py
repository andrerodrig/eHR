from apps.overtime.models import OvertimeRegister
from rest_framework import serializers


class OvertimeRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeRegister
        fields = ('reason', 'employee', 'hours',)
