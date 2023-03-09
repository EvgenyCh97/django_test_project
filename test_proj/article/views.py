from django.shortcuts import render
from test_proj.views import View


class View(View):

    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'article'
        return context
