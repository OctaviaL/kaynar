from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, code):
    send_mail(
        'Фонд помощи животным "Кайнар"', # title
        f'http://35.246.210.249/api/v1/account/activate/{code}/', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )