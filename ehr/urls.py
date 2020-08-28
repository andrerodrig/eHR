from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("apps.core.urls")),
    path("funcionarios/", include("apps.employee.urls")),
    path("documentos/", include("apps.documents.urls")),
    path("horas-extras/", include("apps.overtime.urls")),
    path("departamentos/", include("apps.department.urls")),
    path("empresa/", include("apps.company.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
