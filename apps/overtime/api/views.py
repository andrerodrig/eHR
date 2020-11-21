from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.overtime.api.serializers import OvertimeRegisterSerializer
from apps.overtime.models import OvertimeRegister


class OvertimeRegisterViewSet(viewsets.ModelViewSet):
    queryset = OvertimeRegister.objects.all()
    serializer_class = OvertimeRegisterSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
