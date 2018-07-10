import datetime

from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods


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
