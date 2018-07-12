from django.contrib import admin
from django.urls import path
from blog.articles.views import home
from blog.articles.views import calculate
from blog.articles.views import archiv, articles_num, articles_year

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('calculate/', calculate),
    path('articles/', archiv),  # для вывода архива
    path('articles/<int:id>/', articles_num, name='articles_num'), # для вывода статьи с номером
    path('articles/archive/<int:year>/', articles_year, name='articles_year'),  # для вывода статей по году
]
