from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate
from account.send_mail import send_activation_code

User = get_user_model()

class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(
        required=True,
        min_length=8,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = ('email', 'password', 'password2')
    
    def validate_email(self, email):
        print('Hello')
        return email    

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Ваши пароли не совпадают!')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError('Пользователь не найден!')
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError('Пароль не найден!')
        attrs['user'] = user

        return attrs 

from django.contrib.auth import get_user_model
from account.send_email import send_password_code
# from account.tasks import send_activation_code as celery_register

User = get_user_model()  # CustomUser


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validete_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не существует!')
        
        return email
    
    def send_reset_password_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_password_code(email=email, code=user.activation_code)

    

class ForgotPasswordCompliteSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs
    
    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Неверный код!')
        return code
    
    def set_new_password(self):
        user = User.objects.get(activation_code=self.validated_data.get('code'))
        password = self.validated_data.get('password')
        user.set_password(password)
        user.activation_code = ''
        user.save(update_fields=['password', 'activation_code'])

