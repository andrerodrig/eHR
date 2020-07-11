from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.employee.models import Employee


@login_required
def home(request):
    data = {}
    data['user'] = request.user
    return render(request, 'core/index.html', context=data)
