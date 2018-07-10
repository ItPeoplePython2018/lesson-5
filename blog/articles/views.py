import datetime

from django.http import HttpResponse, HttpRequest, Http404
from django.views.decorators.http import require_http_methods
from blog.articles.models import ARTICLES


def home(request: HttpRequest) -> HttpResponse:
    current_time = datetime.date.today().isoformat()
    return HttpResponse(current_time, content_type='text/plain')


def handler400(request, *args, **kwargs):
    return HttpResponse('Неизвестная операция или деление на ноль', status=400)


@require_http_methods(['GET'])
def calculate(request):
    operation = request.GET['op']
    left_operand = int(request.GET['left'])
    right_operand = int(request.GET['right'])
    print(request.GET, operation, left_operand, right_operand)
    if operation == '+':
        result = left_operand + right_operand
    elif operation == '-':
        result = left_operand - right_operand
    elif operation == '*':
        result = left_operand * right_operand
    elif operation == '/' and right_operand != 0:
        result = left_operand / right_operand
    else:
        return handler400(request)
    return HttpResponse(result)

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
