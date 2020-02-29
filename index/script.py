import os, django

from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joythinkers.settings")
django.setup()
from django.db import models

from index.models import Image
from index.models import Category
from index.models import Size


# C:\Users\david\Desktop\3d foam paper\270300
# "C:/Users/david/Documents/Tencent Files/907266354/"
#                           "FileRecv/instruments&mini furniture/500555"
# C:/Users/david/Downloads/vehicles&vessels/270300
def add_image():
    img_category = Category.objects.get_or_create(main_category="3d Foam Paper Puzzle",
                                                  category="Famous Buildings")
    img_size_270300 = Size.objects.get_or_create(size="270300")
    img_size_500555 = Size.objects.get_or_create(size="500555")
    some_dir = "C:/Users/david/Desktop/3d foam paper/famous building/500x555"
    os.chdir(some_dir)
    for img in os.listdir(some_dir):
        name = img
        name = name.split("(")[0][:-1].replace(" ", "_").replace("&", "")
        Image.objects.create(name=name,
                             product_picture=File(open(img, 'rb')),
                             category=img_category[0],
                             size=img_size_500555[0])


add_image()
