# -*- coding: utf-8 -*-

from django.urls import path
from .views import CompareView


app_name = 'compare'
urlpatterns = [
    path('', CompareView.as_view(), name='compare'),
]