from django import forms
from .models import Account

class TransferMoney(forms.ModelForm):
    class Meta:
        model=Account
        fields=('holder',)
    amount=forms.IntegerField()

class AddBalance(forms.Form):
    amount=forms.IntegerField()


