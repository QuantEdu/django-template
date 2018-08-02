from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'lp/index.html'


class NumIndexView(TemplateView):
    def get_template_names(self):
        return 'lp/index' + str(self.kwargs['number']) + '.html'
