from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from articles.models import ARTICLES


# Create your views here.
def show_all(request):
    return HttpResponse('\n'.join((article['title'] for article in ARTICLES)), content_type='text/plain; charset=utf-8')


def show_specified_article(request, id):
    article_name = ''
    for article in ARTICLES:
        if article['id'] == id:
            article_name = article['title']
    if article_name:
        return HttpResponse(article_name)
    raise Http404


def show_articles_by_year(request, year):
    over_a_year_articles = '\n'.join((article['title'] for article in ARTICLES if article['year'] == year))
    print(over_a_year_articles)
    if over_a_year_articles:
        return HttpResponse(over_a_year_articles, content_type='text/plain; charset=UTF-8')
    raise Http404
