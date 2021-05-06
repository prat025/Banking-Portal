from django.shortcuts import render, redirect
from .models import Account, Transaction_Details
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import AddBalance, TransferMoney

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form=UserCreationForm()
    return render(request, 'bank/signup.html', {'form':form}) 
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            global user
            user=form.get_user()
            login(request, user)
            p=Account.objects.filter(holder=user)
            temp1=p[0].amount
            if temp1>0:
                return redirect('http://127.0.0.1:8000/welcome/')
            else:
                return redirect('http://127.0.0.1:8000/add_balance/')
    else:
        form=AuthenticationForm()
    return render(request, 'bank/login.html', {'form':form})
def log_out(request):
    if request.method=='GET':
        logout(request)
        return redirect('http://127.0.0.1:8000/')
def welcome(request):
        global money
        p=Account.objects.filter(holder=user)
        money=p[0].amount
        return render(request, 'bank/welcome.html',{'money':money}, {'user':p})
def Add_Balance(request):
    if request.method=='GET':
        form=AddBalance()
        return render(request, 'bank/add_balance.html', {'form':form})
    else:
        form=AddBalance(request.POST)
        if form.is_valid():
            g=form.cleaned_data.get("amount") 
            c=g+money
            Account.objects.filter(holder=user).update(amount=c)
            return redirect('http://127.0.0.1:8000/welcome/')
        else:
            form=AddBalance()
            return render(request, 'bank/add_balance.html', {'form':form})

def transfer_money(request):
    if request.method=='GET':
        form=TransferMoney()
        return render(request, 'bank/transfer_money.html', {'form':form})
    else:
        form=TransferMoney(request.POST)
        if form.is_valid():
            g=form.cleaned_data.get("amount")
            beneficiary=form.cleaned_data.get("holder")
            Account.objects.filter(holder=user).update(amount=-g+money)
            y=Account.objects.filter(holder=beneficiary)
            temp2=y[0].amount
            Account.objects.filter(holder=beneficiary).update(amount=temp2+g)
            b=Transaction_Details(transferred_by=user, transferred_to=beneficiary, amount2=g)
            b.save()
            return redirect('http://127.0.0.1:8000/welcome/')
        else:
            form=TransferMoney()
            return render(request, 'bank/transfer_money.html', {'form':form})
def Money_Sent(request):
    if request.method=='GET':
        h=Transaction_Details.objects.filter(transferred_by=user)
        return render(request, 'bank/money_sent.html', {'h':h})
def Money_Received(request):
    if request.method=='GET':
        h1=Transaction_Details.objects.filter(transferred_to=user)
        return render(request, 'bank/money_received.html', {'h1':h1})


            

            

            
            




