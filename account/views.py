from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import RegisterSerializers, LoginSerializer, ForgotPasswordCompliteSerializer, ForgotPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from account.models import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# from social_django.utils import psa

from requests.exceptions import HTTPError

User = get_user_model()

class RegisterAPIView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializers)
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


from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# from social_django.utils import psa

from requests.exceptions import HTTPError


# @api_view(['POST'])
# @permission_classes([AllowAny])
# @psa()
# def register_by_access_token(request, backend):
#     token = request.data.get('access_token')
#     user = request.backend.do_auth(token)
#     print(request)
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(
#             {
#                 'token': token.key
#             },
#             status=status.HTTP_200_OK,
#             )
#     else:
#         return Response(
#             {
#                 'errors': {
#                     'token': 'Invalid token'
#                     }
#             },
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# @api_view(['GET', 'POST'])
# def authentication_test(request):
#     print(request.user)
#     return Response(
#         {
#             'message': "User successfully authenticated"
#         },
#         status=status.HTTP_200_OK,
#     )




# @api_view(['POST'])
# @permission_classes([AllowAny])
# @psa()
# def register_by_access_token(request, backend):
#     token = request.data.get('access_token')
#     user = request.backend.do_auth(token)
#     print(request)
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(
#             {
#                 'token': token.key
#             },
#             status=status.HTTP_200_OK,
#             )
#     else:
#         return Response(
#             {
#                 'errors': {
#                     'token': 'Invalid token'
#                     }
#             },
#             status=status.HTTP_400_BAD_REQUEST,
#         )


# @api_view(['GET', 'POST'])
# def authentication_test(request):
#     print(request.user)
#     return Response(
#         {
#             'message': "User successfully authenticated"
#         },
#         status=status.HTTP_200_OK,
#     )