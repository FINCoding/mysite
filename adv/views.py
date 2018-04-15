from django.shortcuts import render
from adv.models import *
from loginsys.models import *
from mysite.settings import MEDIA_ROOT

def adv(request, adv_id):
    adv = Adv.objects.get(id=adv_id)
     # imagesInAdv = ImageInAdv.objects.get(id=id)
    print(request.user)
    return render(request, 'adv.html', locals())

def add(request):
    user = request.user
    user_email = request.user.email
    user_phone = UserPhone.objects.get(user=request.user)
    return render(request, 'adv_add.html', locals())
