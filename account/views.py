from rest_framework.views import APIView
<<<<<<< HEAD

from account.serializers import *
=======
from rest_framework.response import Response
from account.serializers import RegisterSerializers, LoginSerializer, ForgotPasswordCompliteSerializer, ForgotPasswordSerializer
>>>>>>> 29f9e13c4258fb0f464541c9588f14b38927cb07
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from account.models import *
<<<<<<< HEAD
from account.serializers import  ForgotPasswordCompliteSerializer, ForgotPasswordSerializer
=======
from account.serializers import ForgotPasswordCompliteSerializer, ForgotPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
>>>>>>> 29f9e13c4258fb0f464541c9588f14b38927cb07

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Добро пожаловать в Kaynar! Перейдите на почту для подтверждения своего аккаунта.', status=201)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Успешно', status=200)
        except User.DoesNotExist:
            return Response('Срок действия ссылки истек!', status=400)


class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutAPIView(ObtainAuthToken):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            Token.objects.get(user=user).delete()
            return Response('Вы успешно разлогинились!', status=200)
        except:
            return Response('Ошибка!', status=403)

<<<<<<< HEAD

=======
>>>>>>> 29f9e13c4258fb0f464541c9588f14b38927cb07

class ForgotPasswordAPIView(APIView):
   
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_reset_password_code()
        return Response('Вам отправлено письмо для восстановления пароля.')

class ForgotPasswordCompleteAPIView(APIView):
    
    def post(self, request):
        serializer = ForgotPasswordCompliteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно изменен!')

