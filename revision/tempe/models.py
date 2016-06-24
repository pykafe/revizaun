from __future__ import unicode_literals

from django.db import models

# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return 'District {}'.format(self.name)


class SubDistrict(models.Model):
    name = models.CharField(max_length=25)
    district = models.ForeignKey(District, blank=False, null=False, related_name="subdistrict_set")

    def __unicode__(self):
        return 'Sub-district {}'.format(self.name)


class Suco(models.Model):
    name = models.CharField(max_length=25)
    subdistrict = models.ForeignKey(SubDistrict, blank=False, null=False)

    def __unicode__(self):
        return 'Suco {}'.format(self.name)


class Aldeia(models.Model):
    name = models.CharField(max_length=25)
    suco = models.ForeignKey(Suco, blank=False, null=False)

    def __unicode__(self):
        return 'Aldeia {} Suco {}'.format(self.name, self.suco)


class Tourist(models.Model):
    name = models.CharField(max_length=35)
    aldeias = models.ManyToManyField(Aldeia, related_name='tourists')

    def __unicode__(self):
        return 'Tourist {}'.format(self.name)
