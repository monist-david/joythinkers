# -*- coding: utf-8 -*-

from django.urls import path
from .views import ProductDetailsView, ProductDetailsAffiliateView, ProductDetailsGalleryLeftView, \
    ProductDetailsGalleryRightView, ProductDetailsGroupView, ProductDetailsSliderBoxView, \
    ProductDetailsSliderFullWidthView, ProductDetailsStickyLeftView, ProductDetailsStickyRightView, \
    ProductDetailsTabStyle2View, ProductDetailsTabStyle3View, ProductDetailsVariableView

app_name = 'product_details'
urlpatterns = [
    path('<str:products>/', ProductDetailsView.as_view(), name='product_details'),
    path('product_details_affiliate/', ProductDetailsAffiliateView.as_view(), name='product_details_affiliate'),
    path('product_details_gallery_left/', ProductDetailsGalleryLeftView.as_view(), name='product_details_gallery_left'),
    path('product_details_gallery_right/', ProductDetailsGalleryRightView.as_view(),
         name='product_details_gallery_right'),
    path('product_details_group/', ProductDetailsGroupView.as_view(), name='product_details_group'),
    path('product_details_slider_box/', ProductDetailsSliderBoxView.as_view(), name='product_details_slider_box'),
    path('product_details_slider_full_width/', ProductDetailsSliderFullWidthView.as_view(),
         name='product_details_slider_full_width'),
    path('product_details_sticky_left/', ProductDetailsStickyLeftView.as_view(),
         name='product_details_sticky_left'),
    path('product_details_sticky_right/', ProductDetailsStickyRightView.as_view(),
         name='product_details_sticky_right'),
    path('product_details_tab_style2/', ProductDetailsTabStyle2View.as_view(),
         name='product_details_tab_style2'),
    path('product_details_tab_style3/', ProductDetailsTabStyle3View.as_view(),
         name='product_details_tab_style3'),
    path('product_details_variable/', ProductDetailsVariableView.as_view(),
         name='product_details_variable'),
]
