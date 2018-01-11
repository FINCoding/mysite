
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from channels.channel import Channel

def home(request):
    return render(request, 'chat.html')