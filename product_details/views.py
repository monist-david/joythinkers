from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from index import models
from index.models import Size


class ProductDetailsView(TemplateView):
    template_name = "product_details/product-details.html"

    def get(self, request, products):
        all_product_270300 = models.Image.objects.filter(name=products,
                                                         size=Size.objects.get(size="270300"))
        all_product_500555 = models.Image.objects.filter(name=products, size=Size.objects.get(size="500555"))
        print(all_product_270300)
        context = {'all_product_270300': all_product_270300,
                   'all_product_500555': all_product_500555}

        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsAffiliateView(TemplateView):
    template_name = "product_details/product-details-affiliate.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsGalleryLeftView(TemplateView):
    template_name = "product_details/product-details-gallery-left.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsGalleryRightView(TemplateView):
    template_name = "product_details/product-details-gallery-right.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsGroupView(TemplateView):
    template_name = "product_details/product-details-group.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsSliderBoxView(TemplateView):
    template_name = "product_details/product-details-slider-box.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsSliderFullWidthView(TemplateView):
    template_name = "product_details/product-details-slider-full-width.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsStickyLeftView(TemplateView):
    template_name = "product_details/product-details-sticky-left.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsStickyRightView(TemplateView):
    template_name = "product_details/product-details-sticky-right.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsTabStyle2View(TemplateView):
    template_name = "product_details/product-details-tab-style-2.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsTabStyle3View(TemplateView):
    template_name = "product_details/product-details-tab-style-3.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailsVariableView(TemplateView):
    template_name = "product_details/product-details-variable.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
