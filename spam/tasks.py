from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact 

@shared_task
def send_spam():
    emails = [i.email for i in Contact.objects.all()]
    send_mail(
        'Приют "Кайнар"', # title
        f'Привет! Малыши из нашего приюта уже соскучились по тебе, скорее заходи навестить их!', # body
        'ajkanysdzumagulova@gmail.com', # from
        emails # to
    )