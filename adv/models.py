from django.db import models
from category.models import Category

class Adv(models.Model):
    subj = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, blank=True, null=True, default=True)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Объявление %s от %s" % ( self.id,self.customer_name)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Обявления"

class ImageInAdv(models.Model):
    adv = models.ForeignKey(Adv, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='images_adv/')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Картинки в объявлениях"
        verbose_name_plural = "Картинки в объявлениях"

class Test(models.Model):
    adv = models.ForeignKey(Adv, blank=True, null=True, default=None)
    f = models.CharField(max_length=64, blank=True, null=True, default=None)