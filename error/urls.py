# -*- coding: utf-8 -*-

from django.urls import path
from .views import ErrorView


app_name = 'error'
urlpatterns = [
    path('', ErrorView.as_view(), name='error'),
]