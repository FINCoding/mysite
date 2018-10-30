from django.conf.urls import url, include
from . import views
# from add import views

urlpatterns = [
        url(r'^adv/(?P<adv_id>\w+)/$', views.adv, name = 'adv'),
        url(r'^add/', views.add, name = 'add'),
        ]