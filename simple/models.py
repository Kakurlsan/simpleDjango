#from __future__ import unicode_literals
# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(verbose_name=u"名称", max_length=48, null=False, blank=False, unique=True, db_index=True)
    foreign_name = models.CharField(verbose_name=u"外文名称", max_length=48, null=False, blank=True, default="")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "publisher"
        verbose_name = u'发行方/播出台'
        verbose_name_plural = u'发行方/播出台'