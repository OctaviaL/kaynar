from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Приют для животных "Кайнар"',
        f'Ваш код активации: http://35.246.210.249/api/v1/account/activate/{code}/',
        'ajkanysdzumagulova@gmail.com',
        [email]
    )

def send_password_code(email, code):
    
    send_mail(
        'Вас приветсвует приют для животных "Кайнар"!', # title
        f'Здравствуйте! Чтобы сбросить ваш пароль, вам необходимо знать этот код: {code}', # body
        'ajkanysdzumagulova@gmail.com', # from
        [email] # to
    )