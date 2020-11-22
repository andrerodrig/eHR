from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.employee.models import Employee

# Django Rest dependencies
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

from .tasks import send_report


@login_required
def home(request):
    data = {}
    data['user'] = request.user
    return render(request, 'core/index.html', context=data)


def mail_celery(request):
    send_report.delay()
    return HttpResponse('Task included to the execution queue.')


class UserViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows users to be viewed or edited
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows groups to be viewrd or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classses = [permissions.IsAuthenticated]
