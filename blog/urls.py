from django.contrib import admin
from django.urls import path
from blog.articles.views import (
    home, calculate, articles, articles_detail, articles_year
)

urlpatterns = [
    path('', home),
    path('calculate/', calculate),
    path('articles/', articles),
    path('articles/<int:id>/', articles_detail),
    path('articles/archive/<int:year>/', articles_year),
    path('admin/', admin.site.urls),
]

