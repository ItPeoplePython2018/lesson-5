from django.urls import path
from blog.articles.view import home

urlpatterns = [
  path('', home),
  path('calculate/', calculate),
]
