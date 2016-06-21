from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return 'Country {}'.format(self.name)


class District(models.Model):
    name = models.CharField(max_length=25)
    country = models.ForeignKey(Country, blank=False, null=False)

    def __unicode__(self):
        return 'District {}'.format(self.name)


class SubDistrict(models.Model):
    name = models.CharField(max_length=25)
    district = models.ForeignKey(District, blank=False, null=False)

    def __unicode__(self):
        return 'Sub-district {}'.format(self.name)


class Suco(models.Model):
    name = models.CharField(max_length=25)
    subdistrict = models.ForeignKey(SubDistrict, blank=False, null=False)

    def __unicode__(self):
        return 'Suco {}'.format(self.name)
