from rest_framework import viewsets
from apps.overtime.api.serializers import OvertimeRegisterSerializer
from apps.overtime.models import OvertimeRegister


class OvertimeRegisterViewSet(viewsets.ModelViewSet):
    queryset = OvertimeRegister.objects.all()
    serializer_class = OvertimeRegisterSerializer
