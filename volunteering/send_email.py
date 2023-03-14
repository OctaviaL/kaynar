from django.core.mail import send_mail


def send_order_confirmation_code(email, code, name, price):
    
    full_link = f'Здравствуйте! Подтвердите волонтерство над малышом по имени {name}\n\n http://localhost:8000/api/v1/volunteer/confirm/{code}'

    send_mail(
    'Волонтерство над малышом приюта "Кайнар"',
    full_link,
    'lucifercommander@gmail.com',
    [email]
    )