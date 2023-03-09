from django.shortcuts import render


def index(request):
    app_name = ['Article', 'app']
    return render(request, 'article/index.html', context={'app_name': app_name})
