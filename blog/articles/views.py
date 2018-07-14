from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404
from django.views.decorators.http import require_http_methods
import datetime
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

def archiv (request: HttpRequest):
    rtrn = []
    for i in ARTICLES:
        rtrn.append(i['title'])
    return HttpResponse('\n'.join(rtrn))

def articles_num (request: HttpRequest, id):
    for i in ARTICLES:
        if i['id'] == id:
            return HttpResponse(i['title'])
    return HttpResponse('Нет такой страницы: {}'.format(id), status=404)

def articles_year (request: HttpRequest, year):
    rtrn = []
    for i in ARTICLES:
        if i['year'] == year:
            rtrn.append(i['title'])
    return HttpResponse('\n'.join(rtrn))
