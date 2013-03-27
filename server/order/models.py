from django.db import models
from django.forms import ModelForm

class Order(models.Model):
    customerid  =   models.CharField(max_length=20)
    voltage     =   models.IntegerField()
    current     =   models.IntegerField()
    width       =   models.IntegerField()
    height      =   models.IntegerField()
    order_ts    =   models.DateTimeField(auto_now=True)
    status      =   models.CharField(max_length=20)
    status_ts   =   models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class OrderForm(ModelForm):
    class Meta:
        model = Order
