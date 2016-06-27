from django.views.generic.base import TemplateView
from  .models import District, SubDistrict, Suco, Aldeia, Visitor
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy


class Index(CreateView):
    model = District
    fields = ['name']
    template_name = 'tempe/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        ''' Add a list of subcategories by category to the context '''

        context = super(Index, self).get_context_data(*args, **kwargs)
        context['districts'] = District.objects.all()
        context['subdistricts'] = SubDistrict.objects.all()
        context['sucos'] = Suco.objects.all()
        context['aldeias'] = Aldeia.objects.all()
        context['visitors'] = Visitor.objects.all()
        return context
    
    def get_form(self, form_class):
        form = super(Index, self).get_form(form_class)
        form.fields['name']
        return form
    
    