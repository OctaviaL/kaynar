
def send_activation_code(email, code):

    send_mail(
        'Kaynar',
        f'http://localhost:8000/account/activate/{code}/',
        'ajkanysdzumagulova@gmail.com',
        [email]
    )