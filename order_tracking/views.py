from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class OrderTrackingView(TemplateView):
    template_name = "order_tracking/order-tracking.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
