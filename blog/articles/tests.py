import datetime
import itertools
import urllib.parse

from django.test import TestCase


# Create your tests here.
class RoutesTest(TestCase):
    def setUp(self):
        self.today = datetime.date.today().isoformat().encode('ascii')

    def test_home(self):
        # Добавить в наше приложение обработчик для главной страницы.
        #
        # В теле ответа должно возвращатся текущая дата в формате ISO
        # Для этого можно использовать метод `isoformat` у экземпляра даты.
        response = self.client.get('/')
        assert response.status_code == 200
        assert self.today in response.content

    def test_calculate(self):
        # Добавить в наше приложение обработчик для URL'а `calculate` для проведения
        # математических операций над двумя числами.
        #
        # Аргументы передаются в запросе URL'е:
        # - op - тип операции:
        #   '+' - сложение
        #   '-' - вычитание
        #   '*' = умножения 
        #   '/' = деление 
        # - `left` и `right` - операнды
        #
        # При ошибке (неизвестная операция или деление на 0) отправлять 400 статус
        def calculate(op, left, right):
            op = urllib.parse.quote(op)
            response = self.client.get(f'/calculate/?op={op}&left={left}&right={right}')
            self.assertEquals(response.status_code, 200)
            return float(response.content)

        def calculate_zero(op, left, right):
            op = urllib.parse.quote(op)
            response = self.client.get(f'/calculate/?op={op}&left={left}&right={right}')
            assert response.status_code == 400
            return None

        # декартово произведение: (1, 1), (1, 2), (1, 3), ..., (4, 4)
        for l, r in itertools.product([1, 2, 3, 4], repeat=2):
            self.assertEquals(calculate('+', l, r), l + r)
            self.assertEquals(calculate('-', l, r), l - r)
            self.assertEquals(calculate('*', l, r), l * r)

            if r == 0:
                self.assertIsNone(calculate_zero('/', l, r))
            else:
                self.assertEquals(calculate('/', l, r), l / r)

        self.assertIsNone(calculate_zero('|', 1, 2))

    def test_method(self):
        # Добавить обработчик URL обрабатывающий запросы GET и POST.
        #
        # При запросе GET функция должна
        pass
