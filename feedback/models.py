from django.db import models
from post.models import PetPost
from django.contrib.auth import get_user_model

User = get_user_model()

class Favorite(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    post = models.ForeignKey(
        PetPost,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
