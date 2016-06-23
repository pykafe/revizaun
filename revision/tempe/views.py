from django.views.generic.base import TemplateView
from  .models import District, SubDistrict, Suco, Aldeia, Visitor
from rest_framework import viewsets
from .serializers import DistrictSerializer, SubdistrictSerializer, SucoSerializer, AldeiaSerializer, VisitorSerializer


class Index(TemplateView):
    template_name = 'tempe/index.html'

    def get_context_data(self, *args, **kwargs):
        ''' Add a list of subcategories by category to the context '''

        context = super(Index, self).get_context_data(*args, **kwargs)
        context['districts'] = District.objects.all()
        context['subdistricts'] = SubDistrict.objects.all()
        context['sucos'] = Suco.objects.all()
        context['aldeias'] = Aldeia.objects.all()
        context['visitors'] = Visitor.objects.all()
        return context


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
