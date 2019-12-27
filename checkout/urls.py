# -*- coding: utf-8 -*-

from django.urls import path
from .views import CheckoutView


app_name = 'checkout'
urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
]