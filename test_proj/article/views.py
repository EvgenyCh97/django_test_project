from django.shortcuts import redirect
from django.http import HttpResponse
from test_proj.views import View
from django.urls import reverse


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


def redirect_to_(request):
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


class Index(View):

    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'article'
        return context
