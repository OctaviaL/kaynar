from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from post.tasks import send_product_news



@receiver(post_save, sender=PetPost)    
def post_product(sender, instance, created, **kwargs):
    if created:
        send_product_news.delay(instance.name)