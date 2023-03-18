from celery import shared_task
from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact 


@shared_task
def big_function():
    import time
    time.sleep(10)

@shared_task
def send_product_news(name):
    emails = [i.email for i in Contact.objects.all()]
    send_mail(
        'Приют для животных "Кайнар"', # title
        f'У нас новый друг по имени {name}, скорее заходи знакомиться!!', # body
        'omurbekovaerika@gmail.com', # from
        emails # to
    )