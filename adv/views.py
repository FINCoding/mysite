from django.shortcuts import render
from adv.models import *

def adv(request, adv_id):
    adv = Adv.objects.get(id=adv_id)
    return  render(request, 'adv.html', locals())