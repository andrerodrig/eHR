from django.urls import path
from .views import CompanyCreate


urlpatterns = [
    path("new", CompanyCreate.as_view(), name="create_company"),
]
