from django.urls import path
from . import views as v


urlpatterns = [
    path("new/", v.CompanyCreate.as_view(), name="create_company"),
    path("edit/<int:pk>/", v.CompanyEdit.as_view(), name="edit_company"),
]
