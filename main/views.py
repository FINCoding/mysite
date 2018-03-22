from django.shortcuts import render
from .forms import SubscriberForm
from adv.models import *
from django.contrib import auth
# from django

def main(request):
    # form = SubscriberForm(request.POST or None)
    advs = Adv.objects.filter(is_active=True)
    username = auth.get_user(request).username
    # if request.method == "POST":
    #     print(form)
    #     new_form = form.save()
    return render(request, 'main.html', locals() )


