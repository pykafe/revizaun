from django.views.generic.base import TemplateView
from  .models import District, SubDistrict, Suco, Aldeia, Visitor
from rest_framework import viewsets
from .serializers import DistrictSerializer, SubdistrictSerializer, SucoSerializer, AldeiaSerializer, VisitorSerializer


class Index(TemplateView):
    template_name = 'tempe/index.html'


class DistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class SubdistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SubDistrict.objects.all()
    serializer_class = SubdistrictSerializer


class SucoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Suco.objects.all()
    serializer_class = SucoSerializer


class AldeiaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Aldeia.objects.all()
    serializer_class = AldeiaSerializer


class VisitorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
