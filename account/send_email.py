from django.core.mail import send_mail

def send_password_code(email, code):
    send_mail(
        'Вас приветсвует приют для животных "Кайнар"!', # title
        f'Здравствуйте! Чтобы сбросить ваш пароль, вам необходимо знать этот код: {code}', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )