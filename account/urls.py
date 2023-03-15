from django.urls import path, re_path
from account.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from account.views import ForgotPasswordAPIView, ForgotPasswordCompleteAPIView
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('reset_password/', ForgotPasswordAPIView.as_view()),
    path('reset_password_complete/', ForgotPasswordCompleteAPIView.as_view()),

    re_path('api/register-by-access-token/' + r'social/(?P<backend>[^/]+)/$', views.register_by_access_token),
    path('api/authentication-test/', views.authentication_test),
    
]