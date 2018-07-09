from django.urls import path
from blog.articles.views import show_all, show_specified_article, show_articles_by_year

urlpatterns = [
    path('', show_all),
    path('<int:id>', show_specified_article),
    path('archive/<int:year>', show_articles_by_year),
]
