# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser


class UserPhone(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(verbose_name='Введите номер телефона',
                                    max_length= 128)

    objects = UserManager()
    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

