import os

from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    # remove path separators from filename
    filename = os.path.basename(filename)
    return f'uploads/user_{instance.author.id}/{filename}'


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='insta_post', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to, default='/grey_background.jpg')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default='1')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f'{self.user} ({self.created_at:%d-%m-%Y %H:%M}) {self.body}'

    class Meta:
        ordering = ['-created_at']

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def can_edit(self, user):
        return self.author == user


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.post} {self.text}'
