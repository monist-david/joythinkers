from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "contact/contact-us.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
