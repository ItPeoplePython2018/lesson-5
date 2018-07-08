import datetime
import itertools
import urllib.parse

from django.test import TestCase


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
        # Добавить в наше приложение обработчик для URL'а `calculate`
        # для проведения математических операций над двумя числами.
        #
        # Аргументы передаются в запросе URL'е:
        # - `op` - тип операции:
        #   * '+' - сложение
        #   * '-' - вычитание
        #   * '*' = умножения
        #   * '/' = деление
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

    def test_articles(self):
        # Добавить обработчики для архива статей:
        #
        # 1. Со списком всех статей (`articles/`),
        #    возвращает названия статей разделенных переносом строки ('\n`)
        # 2. С отдельной статьи (`articles/3/`),
        #    возвращает название отдельной статьи, если она отсуствует - вернуть статус 404.
        # 3. Со списком статей за отдельный год (`articles/archive/2012/`),
        #    возвращает названия статей разделенных переносом строки ('\n`)
        #
        # Все шаблоны и обработчики URL должны находиться в пакете `blog.articles`.
        #
        # Данные для вывода находяться в словаре `ARTICLES` в модуле
        # `blog.articles.models`.
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, ('\n'.join([
            'Заглавная статья',
            'Вышел Python 3.6',
            'Вышел Python 3.7'
        ])).encode('utf-8'))

        response = self.client.get('/articles/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Заглавная статья'.encode('utf-8'))

        response = self.client.get('/articles/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Вышел Python 3.6'.encode('utf-8'))

        response = self.client.get('/articles/3/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Вышел Python 3.7'.encode('utf-8'))

        response = self.client.get('/articles/4/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/articles/archive/2016/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')

        response = self.client.get('/articles/archive/2017/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, ('\n'.join([
            'Заглавная статья',
            'Вышел Python 3.6',
        ])).encode('utf-8'))

        response = self.client.get('/articles/archive/2018/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, ('\n'.join([
            'Вышел Python 3.7'
        ])).encode('utf-8'))
