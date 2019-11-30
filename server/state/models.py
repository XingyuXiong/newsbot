from django.db import models


class State(models.Model):
    'blank=True is not needed with more accurate sql queries'
    'null=True should be avoided'
    answer = models.CharField(max_length=256,null=True,blank=True)
    state = models.IntegerField(null=True,blank=True)
    intent = models.CharField(max_length=64,null=True,blank=True)
    addition = models.CharField(max_length=64,null=True,blank=True)
    timestep = models.IntegerField(null=True,blank=True)