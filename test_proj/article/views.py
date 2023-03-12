from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from test_proj.views import View
from test_proj.article.models import Article, Comment


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


def redirect_to_(request):
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15:-1]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article
        })


class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'],
                                    article_id=kwargs['article_id'])
        return render(request, 'articles/show.html', context={
            'comment': comment
        })
