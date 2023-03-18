from django.core.mail import send_mail


def send_order_confirmation_code(email, code, name, price):
    
    full_link = f'Здравствуйте! Подтвердите волонтерство над малышом по имени {name}\n\n http://35.246.210.249/api/v1/volunteer/confirm/{code}'

    send_mail(
    'Волонтерство над малышом приюта "Кайнар"',
    full_link,
    'ajkanysdzumagulova@gmail.com',
    [email]
    )