from django.db import models
from django.forms import ModelForm
from factoryState.models import FactoryState
from django.template.loader import render_to_string

class Command(models.Model):
    command  =   models.CharField(max_length=20)
    commandTimeStamp    =   models.DateTimeField(auto_now=True)
    parameter=models.FloatField()
    quantity=models.IntegerField()
    status      =   models.CharField(max_length=20)
    statusTimeStamp   =   models.DateTimeField(auto_now=True)
    description = models.TextField()
    json = models.TextField()

    def __unicode__(self):
        return self.command
