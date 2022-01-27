from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('user_registration/', RegisterUser.as_view()),
    path('user_verification/', VerifyUser.as_view()),
    path('forget_password/', forget_password),
    path('reset_password/', ResetPassword.as_view()),
    path('change_password/', change_password, name='change_password'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]



