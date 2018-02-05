from django.conf.urls import url, include
from adv import views

urlpatterns = [
        url(r'^adv/(?P<adv_id>\w+)/$', views.adv, name = 'adv'),
        ]