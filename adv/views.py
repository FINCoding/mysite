from django.shortcuts import render
from adv.models import *

def adv(request, imageInAdv_id):
    adv = Adv.objects.get(id=imageInAdv_id)
    imagesInAdv = ImageInAdv.objects.get(id=imageInAdv_id)
    return  render(request, 'adv.html', locals())
