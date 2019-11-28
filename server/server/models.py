from django.db import models


class State(models.Model):
    answer = models.CharField(max_length=128)
    state = models.IntegerField()
    intent = models.CharField(max_length=32)
    addition = models.CharField(max_length=32)
    timestep = models.IntegerField()