from django.views.generic.base import TemplateView
from .models import District, SubDistrict, Suco, Aldeia, Tourist


class Index(TemplateView):
    template_name = 'tempe/index.html'

    def get_context_data(self, *args, **kwargs):
        ''' Add a list of subcategories by category to the context '''

        context = super(Index, self).get_context_data(*args, **kwargs)
        context['aldeias'] = Aldeia.objects.all()
        context['tourists'] = Tourist.objects.all()
        return context
