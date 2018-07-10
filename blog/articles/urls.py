from django.urls import path
from blog.articles.views import home, calculate
from blog.articles.views import show_all, show_specified_article, show_articles_by_year

urlpatterns = [
  path('', home),
  path('calculate/', calculate),
  path('articles/', show_all),
  path('articles/<int:id>/', show_specified_article),
  path('articles/archive/<int:year>/', show_articles_by_year),
]
