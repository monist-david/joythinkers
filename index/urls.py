# -*- coding: utf-8 -*-

from django.urls import path
from .views import IndexView, Index02View


app_name = 'index'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index_02/', Index02View.as_view(), name='index_02'),
]