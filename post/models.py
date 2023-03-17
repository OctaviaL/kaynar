from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from post.tasks import send_product_news


User = get_user_model()

class PetPost(models.Model):
    CHOICES1 = (
        ('dogs', 'собаки'),
        ('cats', 'кошки'),
    )

    CHOICES2 = (
        ('male', 'мальчик'),
        ('female', 'девочка'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='petposts')
    name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    gender = models.CharField(choices=CHOICES2, max_length=10)
    description = models.TextField()
    category = models.CharField(choices=CHOICES1, max_length=20)
    # image = models.ForeignKey('PetImage', on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return f'{self.name}'


class PetImage(models.Model):
    name = models.ForeignKey(PetPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return f'{self.image}'
    

@receiver(post_save, sender=PetPost)    
def post_product(sender, instance, created, **kwargs):
    if created:
        send_product_news.delay(instance.name)
from django.contrib.auth import get_user_model


