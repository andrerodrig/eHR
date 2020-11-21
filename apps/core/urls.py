from django.urls import path, include
from . import views as v


app_name = 'core'

urlpatterns = [
    path('', v.home, name='home'),
]
