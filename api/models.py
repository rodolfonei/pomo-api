from django.db import models

class Pomo(models.Model):
    name = models.CharField(max_length=60)
    observation = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='pomos', on_delete=models.CASCADE) 
