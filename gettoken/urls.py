from django.urls import re_path
from . import views

urlpatterns = [
    re_path('ssocallback', views.ssoCallback, name='SSO_Callback'),
    re_path('input', views.inputOauth, name='Oauth'),
    re_path('result', views.result, name='Result'),
    re_path('health', views.health, name='Health'),
]