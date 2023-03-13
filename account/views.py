from rest_framework.views import APIView
from account.serializers import RegisterSerializer, ForgotPasswordCompliteSerializer, ForgotPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

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
