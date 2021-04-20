from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount=models.IntegerField(null=True)
class Transaction_Details(models.Model):
    transferred_by=models.CharField(max_length=30)
    transferred_to=models.CharField(max_length=30)
    amount2=models.IntegerField(null=True)