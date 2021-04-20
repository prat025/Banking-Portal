from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('add_balance/', views.Add_Balance, name='Add_Balance'),
    path('transfer_money/', views.transfer_money, name='Transfer_money'),
    path('money_sent/', views.Money_Sent, name='Money_Sent'),
    
]