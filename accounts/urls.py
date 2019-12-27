# -*- coding: utf-8 -*-

from django.urls import path
from .views import AccountView, LoginRegisterView


app_name = 'accounts'
urlpatterns = [
    path('', AccountView.as_view(), name='accounts'),
    path('login_register/', LoginRegisterView.as_view(), name='login_register')
]