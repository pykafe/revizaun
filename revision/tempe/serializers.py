from models import District, SubDistrict, Suco, Aldeia, Tourist
from rest_framework import serializers


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = ('url', 'name')


class SubDistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubDistrict
        fields = ('url', 'name', 'district')


class SucoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suco
        fields = ('url', 'name', 'subdistrict')


class AldeiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aldeia
        fields = ('url', 'name', 'suco')


class TouristSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tourist
        fields = ('url', 'name', 'aldeias')
