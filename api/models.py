from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Pomo(models.Model):
    name = models.CharField(max_length=60)
    observation = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='pomos', on_delete=models.CASCADE) 

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)