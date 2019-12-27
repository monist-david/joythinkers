# -*- coding: utf-8 -*-

from django.urls import path
from .views import BlogView, Blog01columnView, Blog02columnsView, Blog03columnsView, BlogDetailsAudioView, \
    BlogDetailsGalleryView, BlogDetailsImageView, BlogDetailsVideoView, BlogLeftSidebarView


app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blog_01_column', Blog01columnView.as_view(), name='blog_01_column'),
    path('blog_02_columns', Blog02columnsView.as_view(), name='blog_02_columns'),
    path('blog_03_columns', Blog03columnsView.as_view(), name='blog_03_columns'),
    path('blog_details_audio', BlogDetailsAudioView.as_view(), name='blog_details_audio'),
    path('blog_details_gallery', BlogDetailsGalleryView.as_view(), name='blog_details_gallery'),
    path('blog_details_image', BlogDetailsImageView.as_view(), name='blog_details_image'),
    path('blog_details_video', BlogDetailsVideoView.as_view(), name='blog_details_video'),
    path('blog_left_sidebar', BlogLeftSidebarView.as_view(), name='blog_left_sidebar'),
]