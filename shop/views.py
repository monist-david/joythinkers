from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ShopView(TemplateView):
    template_name = "shop/shop.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopFourColumnsView(TemplateView):
    template_name = "shop/shop-four-columns.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopFullwidthView(TemplateView):
    template_name = "shop/shop-fullwidth.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopListView(TemplateView):
    template_name = "shop/shop-list.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopListRightSidebarView(TemplateView):
    template_name = "shop/shop-list-right-sidebar.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopListSidebarView(TemplateView):
    template_name = "shop/shop-list-sidebar.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopRightSidebarView(TemplateView):
    template_name = "shop/shop-right-sidebar.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ShopThreeColumnsView(TemplateView):
    template_name = "shop/shop-three-columns.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)