from django.urls import path
from test_proj.article import views

urlpatterns = [
    path('', views.View.as_view()),
]
