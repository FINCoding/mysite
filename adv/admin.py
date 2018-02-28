from django.contrib import admin
from .models import *

class ImageInAdvInline(admin.TabularInline):
    model = ImageInAdv
    extra = 0

class AdvAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Adv._meta.fields]
    inlines = [ImageInAdvInline]
    class Meta:
        model = Adv

admin.site.register(Adv, AdvAdmin)


class ImageInAdvAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImageInAdv._meta.fields]

    class Meta:
        model = ImageInAdv

admin.site.register(ImageInAdv, ImageInAdvAdmin)

class testAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Test._meta.fields]

admin.site.register(Test, testAdmin)