from django.urls import path
from test_proj.article import views

urlpatterns = [
    path('', views.redirect_to_),
    path('<str:tags>/<int:article_id>/', views.index, name='article')
]
