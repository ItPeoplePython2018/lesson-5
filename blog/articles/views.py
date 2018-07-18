from django.http import HttpRequest, HttpResponse
import datetime
from blog.articles.models import ARTICLES


def home(request: HttpRequest) -> HttpResponse:
    now = datetime.datetime.now().isoformat()
    return HttpResponse(now, content_type='text/plain; charset=utf-8' )


def calculate(request: HttpRequest) -> HttpResponse:

    print(request.GET)
    if 'op' in request.GET and request.GET.get('op') in (' ', '+','-','*','/'):
        op = request.GET.get('op').replace(' ', '+') #костыль для работы "+" из браузера =)
    else:
        op = "Wrong Operation {}".format(request.GET.get('op'))

    if 'left' in request.GET:
        left = request.GET.get('left')
    else:
        return HttpResponse("Left: Empty parameter", status=400, content_type='text/plain; charset=utf-8' )

    if 'right' in request.GET:
        right = request.GET.get('right')
    else:
        return HttpResponse("Right: Empty parameter".format(request.GET.get('right')), status=400, content_type='text/plain; charset=utf-8' )

    try:
        left_int = int(left)
    except ValueError:
        return HttpResponse("Left: Incorrect value: ".format(request.GET.get('left')), status=400, content_type='text/plain; charset=utf-8' )

    try:
        right_int = int(right)
    except ValueError:
        return HttpResponse("Right: Incorrect value: {}".format(request.GET.get('right')), status=400, content_type='text/plain; charset=utf-8' )

    if op == '+':
        result = left_int + right_int

    elif op == '-':
        result = left_int - right_int

    elif op == '*':
        result = left_int * right_int

    elif op == '/' and right_int != '0':
        result = left_int / right_int

    else:
        return HttpResponse("Что-то пошло не так", status=400, content_type='text/plain; charset=utf-8' )

    return HttpResponse(result)

def articles(request: HttpRequest) -> HttpResponse:
    list = []
    for article in ARTICLES:
        list.append(article['title'])
    return HttpResponse('\n'.join(list), content_type='text/plain; charset=utf-8' )

def articles_detail(request: HttpRequest, id) -> HttpResponse:
    for article in ARTICLES:
        if article['id'] == id:
            return HttpResponse(article['title'], content_type='text/plain; charset=utf-8')

    return HttpResponse("Cтатьи с id: {} не существует".format(id), status=404)

def articles_year(request: HttpRequest, year) -> HttpResponse:
    list = []
    for article in ARTICLES:
        if article['year'] == year:
            list.append(article['title'])
    #тесты хотят чтобы вернулось пусто :(
    #if len(list) == 0:
    #    return HttpResponse("Нет статей за этот год :(", content_type='text/plain; charset=utf-8')
    return HttpResponse('\n'.join(list), content_type='text/plain; charset=utf-8')