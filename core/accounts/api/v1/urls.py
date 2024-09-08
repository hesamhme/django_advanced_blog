from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registrations/', views.RegistrationsApiView.as_view(), name='registrations'),
    # change password
    # reset password
    # login token
    path('token/login/', ObtainAuthToken.as_view() , name='token-login'),
    # login jwt
] 