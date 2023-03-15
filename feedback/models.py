from django.db import models
from post.models import PetPost
from django.contrib.auth import get_user_model

User = get_user_model()
class Like(models.Model):
    """
        Модель лайков
    """

    post = models.ForeignKey(
        PetPost,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.post}'
    

class Comment(models.Model):
    post_comment = models.ForeignKey(PetPost, on_delete=models.CASCADE, related_name='comments') # пост 
   
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    




  