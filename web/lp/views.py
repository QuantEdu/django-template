from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import LeadForm


class IndexView(FormView):
    template_name = 'lp/index.html'
    form_class = LeadForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.create_lead(form)
        return super().form_valid(form)


class NumIndexView(TemplateView):
    def get_template_names(self):
        return 'lp/index' + str(self.kwargs['number']) + '.html'
