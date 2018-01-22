from django.shortcuts import render
from .forms import SubscriberForm

def main(request):
    name = 'Abdul'
    form = SubscriberForm(request.POST or None)
    if request.method == "POST":
        print(form)
        new_form = form.save()
    return render(request, 'main.html', locals() )

