from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from index import models
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .templatetags import printname


class ShopView(TemplateView):
    template_name = "shop/shop.html"

    def get(self, request, category):
        all_product = models.Image.objects.filter(category__main_category=category)
        if not all_product:
            all_product = models.Image.objects.filter(category__category=category)
        all_category = models.Category.objects.filter(main_category=category)
        if not all_category:
            all_category = models.Category.objects.filter(category=category)
            all_category = models.Category.objects.filter(main_category=all_category[0].main_category)
        all_products = []
        for product in all_product:
            if printname.hasNumber(product.product_picture.name):
                all_products.append(product)
        paginator = Paginator(all_products, 8)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            all_products = paginator.page(page)
        except (EmptyPage, InvalidPage):
            all_products = paginator.page(paginator.num_pages)

        context = {'all_products': all_products,
                   'all_category': all_category}
        return render(request, self.template_name, context)

    def post(self, request, category):
        print(category)
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
