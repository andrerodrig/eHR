# Django depencendes
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Django Rest Framework dependencies
from rest_framework import routers

# Internal apps dependencies
from apps.core import views as v
from apps.employee.api.views import EmployeeViewSet
from apps.overtime.api.views import OvertimeRegisterViewSet

# API Routes
router = routers.DefaultRouter()
router.register(r'users', v.UserViewSet)
router.register(r'groups', v.GroupViewSet)
router.register(r'api/funcionarios', EmployeeViewSet)
router.register(r'api/banco-de-horas', OvertimeRegisterViewSet)


urlpatterns = [
    # Home (/index)
    path("", include("apps.core.urls")),
    # /funcionarios
    path("funcionarios/", include("apps.employee.urls")),
    # /documentos
    path("documentos/", include("apps.documents.urls")),
    # /horas-extras
    path("horas-extras/", include("apps.overtime.urls")),
    # /departamentos
    path("departamentos/", include("apps.department.urls")),
    # /empresa
    path("empresa/", include("apps.company.urls")),
    # /accounts
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),


    path('', include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
