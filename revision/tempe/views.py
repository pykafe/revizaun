from django.views.generic.base import TemplateView
from rest_framework import viewsets
from serializers import DistrictSerializer, SubDistrictSerializer, SucoSerializer
from .models import District, SubDistrict, Suco


class Index(TemplateView):
    template_name = 'tempe/index.html'


class DistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class SubDistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SubDistrict.objects.all()
    serializer_class = SubDistrictSerializer


class SucoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Suco.objects.all()
    serializer_class = SucoSerializer
