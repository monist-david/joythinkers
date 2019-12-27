# -*- coding: utf-8 -*-

from django.urls import path
from .views import OrderTrackingView


app_name = 'order_tracking'
urlpatterns = [
    path('', OrderTrackingView.as_view(), name='order_tracking'),
]