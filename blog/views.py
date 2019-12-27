from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class Blog01columnView(TemplateView):
    template_name = "blog/blog-01-column.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class Blog02columnsView(TemplateView):
    template_name = "blog/blog-02-columns.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class Blog03columnsView(TemplateView):
    template_name = "blog/blog-03-columns.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class BlogDetailsAudioView(TemplateView):
    template_name = "blog/blog-details-audio.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class BlogDetailsGalleryView(TemplateView):
    template_name = "blog/blog-details-gallery.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class BlogDetailsImageView(TemplateView):
    template_name = "blog/blog-details-image.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class BlogDetailsVideoView(TemplateView):
    template_name = "blog/blog-details-video.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class BlogLeftSidebarView(TemplateView):
    template_name = "blog/blog-left-sidebar.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

