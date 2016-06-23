from rest_framework import serializers
from .models import District, SubDistrict, Suco, Aldeia, Visitor


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = ('url', 'name')


class SubdistrictSerializer(serializers.HyperlinkedModelSerializer):
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


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = ('url', 'name', 'nationality', 'aldeias')
