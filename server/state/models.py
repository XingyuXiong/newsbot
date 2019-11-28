from django.db import models


class State(models.Model):
    answer = models.CharField(max_length=128,null=True)
    state = models.IntegerField()
    intent = models.CharField(max_length=32,null=True)
    addition = models.CharField(max_length=32,null=True)
    timestep = models.IntegerField()