"""joythinkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from joythinkers import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
    path('error/', include('error.urls', namespace='error')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('product_details/', include('product_details.urls', namespace='product_details')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('compare/', include('compare.urls', namespace='compare')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('order_tracking/', include('order_tracking.urls', namespace='order_tracking')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
