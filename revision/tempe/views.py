from django.views.generic.base import TemplateView
from .models import District, SubDistrict, Suco, Aldeia, Tourist
from rest_framework import viewsets
from serializers import DistrictSerializer, SubDistrictSerializer, SucoSerializer, AldeiaSerializer, TouristSerializer


class Index(TemplateView):
    template_name = 'tempe/index.html'

    def get_context_data(self, *args, **kwargs):
        ''' Add a list of subcategories by category to the context '''

        context = super(Index, self).get_context_data(*args, **kwargs)
        context['districts'] = District.objects.all()
        context['subdistricts'] = SubDistrict.objects.all()
        context['sucos'] = Suco.objects.all()
        context['aldeias'] = Aldeia.objects.all()
        context['tourists'] = Tourist.objects.all()
        return context


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


class AldeiaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aldeia.objects.all()
    serializer_class = AldeiaSerializer


class TouristViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
