from django.urls import path
from rest_framework.authtoken import views
from .views import run_algorithm

urlpatterns = [
    path('run-algorithm/', run_algorithm),
]
