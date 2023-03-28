from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    updated_at = models.DateTimeField(User, auto_now=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_pic', verbose_name='profile_pic')

    def __str__(self):
        return f'{self.user.username}'


# Create Profile When New User Sign Up
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have The User Follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
