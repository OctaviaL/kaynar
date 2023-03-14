from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Kaynar',
        f'http://localhost:8000/account/activate/{code}/',
        'ajkanysdzumagulova@gmail.com',
        [email]
    )

def send_password_code(email, code):
    send_mail(
        'Вас приветсвует приют для животных "Кайнар"!', # title
        f'Здравствуйте! Чтобы сбросить ваш пароль, вам необходимо знать этот код: {code}', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )