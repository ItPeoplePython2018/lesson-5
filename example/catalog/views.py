from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from catalog.models import Article


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    current_time = datetime.date.today().isoformat()
    return HttpResponse(current_time, content_type='text/plain')

def articles_list(request):
    return HttpResponse('Список статей')

def articles_detail(request, id):
    # request.GET
    if 'name' in request.GET:
        request.session['name'] = request.GET['name']
    name = request.session.get('name', "Аноним")
    print(request.META)

    url = reverse('articles_detail', kwargs={'id': 10})
    return HttpResponse('Статья {}: {} [{}]'.format(id, url, name))

def handler404(request, *args, **kwargs):
    return HttpResponse('Не найдено', status=404)

def handler400(request, *args, **kwargs):
    return HttpResponse('Неизвестная операция или деление на ноль', status=400)

def articles_redirect(request):
    return redirect('articles_detail', id=10)

@require_http_methods(['GET'])
def calculate(request):
    operation = request.GET['op']
    left_oparand = int(request.GET['left'])
    right_operand = int(request.GET['right'])
    if operation in ('+', ' '):
        result = left_oparand + right_operand
    elif operation == '-':
        result = left_oparand - right_operand
    elif operation == '*':
        result = left_oparand * right_operand
    elif operation == '/' and right_operand != 0:
        result = left_oparand / right_operand
    else:
        return handler400(request)
    return HttpResponse(result)
