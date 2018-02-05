from django.shortcuts import render
from .forms import SubscriberForm
from adv.models import Adv, ProductInAdv

def main(request):
    name = 'Abdul'
    form = SubscriberForm(request.POST or None)
    advs = Adv.objects.filter(is_active=True)
    productsInAdv = ProductInAdv.objects.filter()
    if request.method == "POST":
        print(form)
        new_form = form.save()
    return render(request, 'main.html', locals() )


