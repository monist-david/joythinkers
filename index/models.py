import os

from django.db import models

from joythinkers import settings


class Image(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    product_picture = models.ImageField(upload_to='500555/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE, default="", null=True, blank=True)

    def __str__(self):
        return str(self.category) + ": " + str(self.product_picture) + "  size  " + str(self.size)


class Category(models.Model):
    main_category = models.CharField(max_length=40, default="", blank=True)
    category = models.CharField(max_length=40, default="", blank=True)

    def __str__(self):
        return self.main_category + ": " + str(self.category)


class Size(models.Model):
    size = models.CharField(default='', max_length=10)

    def __str__(self):
        return self.size
