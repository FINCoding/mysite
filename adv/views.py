from django.shortcuts import render
from adv.models import *
from mysite.settings import MEDIA_ROOT

def adv(request, adv_id):
    adv = Adv.objects.get(id=adv_id)
    print(MEDIA_ROOT)
    # imagesInAdv = ImageInAdv.objects.get(id=id)
    return  render(request, 'adv.html', locals())
