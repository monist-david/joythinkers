# -*- coding: utf-8 -*-

from django.urls import path
from .views import ShopView, ShopFourColumnsView, ShopFullwidthView, ShopListView,\
    ShopListRightSidebarView, ShopListSidebarView, ShopRightSidebarView, ShopThreeColumnsView


app_name = 'shop'
urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('shop_four_columns/', ShopFourColumnsView.as_view(), name='shop_four_columns'),
    path('shop_full_width/', ShopFullwidthView.as_view(), name='shop_full_width'),
    path('shop_list/', ShopListView.as_view(), name='shop_list'),
    path('shop_list_right_sidebar/', ShopListRightSidebarView.as_view(), name='shop_list_right_sidebar'),
    path('shop_list_sidebar/', ShopListSidebarView.as_view(), name='shop_list_sidebar'),
    path('shop_right_sidebar/', ShopRightSidebarView.as_view(), name='shop_right_sidebar'),
    path('shop_three_columns/', ShopThreeColumnsView.as_view(), name='shop_three_columns'),
]