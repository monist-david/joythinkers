from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class WishlistView(TemplateView):
    template_name = "wishlist/wishlist.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
