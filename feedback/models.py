from django.db import models
from post.models import PetPost
from django.contrib.auth import get_user_model

User = get_user_model()

class Like(models.Model):
    """
        Модель поглаживаний
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    post = models.ForeignKey(
        PetPost,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.post}'
    

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(PetPost, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.owner} -> {self.post.name}'
    

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

class Rating(models.Model):
    RATING = (
        ('Солнышко', 'Солнышко'),
        ('Сырничек', 'Сырничек'),
        ('Малышочек', 'Малышочек'),
        ('Круассанчик', 'Круассанчик'),
        ('Сладкая булочка', 'Сладкая булочка')
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    post = models.ForeignKey(
        PetPost,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.CharField(max_length=50, choices=RATING)

    def __str__(self) -> str:
        return f'{self.owner} --> {self.post.name}'
    



