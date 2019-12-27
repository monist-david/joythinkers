from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class CheckoutView(TemplateView):
    template_name = "checkout/checkout.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
