from django.urls import path
from account.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from account.views import ForgotPasswordAPIView, ForgotPasswordCompleteAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
<<<<<<< HEAD
]

urlpatterns = [
#     path('register/', RegisterAPIView.as_view()),
#     path('activate/<uuid:activation_code>/', ActivationView.as_view()),

#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
=======
>>>>>>> 29f9e13c4258fb0f464541c9588f14b38927cb07

    path('reset_password/', ForgotPasswordAPIView.as_view()),
    path('reset_password_complete/', ForgotPasswordCompleteAPIView.as_view()),
    
]