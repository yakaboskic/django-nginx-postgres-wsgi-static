from django.urls import path
from rest_framework.authtoken import views
from .views import run_algorithm, password_auth, pubkey_auth
from .form_views import UserFileView

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('run-algorithm/', run_algorithm),
    path('password', password_auth, name='password_auth'),
    path('pubkey', pubkey_auth, name='pubkey_auth'),
    path('form/', UserFileView.as_view(), name='form')
]