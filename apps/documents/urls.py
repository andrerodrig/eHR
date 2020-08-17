from django.urls import path
from . import views as v


app_name = 'documents'

urlpatterns = [
    path('new/<int:employee_pk>/',
         v.DocumentCreate.as_view(), name='create_document'),
]
