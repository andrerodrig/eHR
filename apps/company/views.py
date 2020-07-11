from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Company


class CompanyCreate(CreateView):
    model = Company
    fields = ["name"]
