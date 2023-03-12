from django.urls import path
from test_proj.article import views
from test_proj.article.views import ArticleView, ArticleCommentsView

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
    path('<int:id>/', ArticleView.as_view()),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]
