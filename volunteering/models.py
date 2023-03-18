import uuid
from django.db import models
from django.contrib.auth import get_user_model
from post.models import PetPost


User = get_user_model()

class Volunteer(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pets'
    )
    animal = models.ForeignKey(
        PetPost,
        on_delete=models.CASCADE,
        related_name='pets'
    )

    is_confirm = models.BooleanField(default=False)
    addres = models.TextField()
    number = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.UUIDField(default=uuid.uuid4)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
