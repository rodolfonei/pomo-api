from django.db import models

class Pomo(models.Model):
    name = models.CharField(max_length=60)
    observation = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
