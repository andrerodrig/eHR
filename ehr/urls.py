from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("apps.core.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("funcionarios/", include("apps.employee.urls")),
    path("departamentos/", include("apps.department.urls")),
    path("empresa/", include("apps.company.urls")),
    path("admin/", admin.site.urls),
]
