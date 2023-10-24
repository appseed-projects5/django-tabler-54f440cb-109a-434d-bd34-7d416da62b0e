# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Thong Ke(models.Model):

    #__Thong Ke_FIELDS__
    madonvi = models.CharField(max_length=255, null=True, blank=True)
    tendonvi = models.CharField(max_length=255, null=True, blank=True)
    phantramxulydunghan = models.CharField(max_length=255, null=True, blank=True)
    tongxulytrehan = models.CharField(max_length=255, null=True, blank=True)
    tongxulydunghan = models.CharField(max_length=255, null=True, blank=True)
    tongchuaxuly = models.CharField(max_length=255, null=True, blank=True)
    tongdaxuly = models.CharField(max_length=255, null=True, blank=True)
    phantramchuaxulytronghan = models.CharField(max_length=255, null=True, blank=True)
    tongsoxuly = models.CharField(max_length=255, null=True, blank=True)
    tongchuaxulytrehan = models.CharField(max_length=255, null=True, blank=True)
    sonhantrongky = models.CharField(max_length=255, null=True, blank=True)
    sotonkytruoc = models.CharField(max_length=255, null=True, blank=True)
    phantramxulytrehan = models.CharField(max_length=255, null=True, blank=True)
    tongchuaxulytronghan = models.CharField(max_length=255, null=True, blank=True)
    phantramchuaxulytrehan = models.CharField(max_length=255, null=True, blank=True)
    loaithongke = models.CharField(max_length=255, null=True, blank=True)
    thang = models.CharField(max_length=255, null=True, blank=True)
    nam = models.CharField(max_length=255, null=True, blank=True)

    #__Thong Ke_FIELDS__END

    class Meta:
        verbose_name        = _("Thong Ke")
        verbose_name_plural = _("Thong Ke")



#__MODELS__END
