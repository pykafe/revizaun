from models import District, SubDistrict, Suco
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
