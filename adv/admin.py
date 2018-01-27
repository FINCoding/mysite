from django.contrib import admin
from .models import *

class ProductInAdvInline(admin.TabularInline):
    model = ProductInAdv
    extra = 0

class AdvAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Adv._meta.fields]
    inlines = [ProductInAdvInline]
    class Meta:
        model = Adv

admin.site.register(Adv, AdvAdmin)


class ProductInAdvAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInAdv._meta.fields]

    class Meta:
        model = ProductInAdv

admin.site.register(ProductInAdv, ProductInAdvAdmin)