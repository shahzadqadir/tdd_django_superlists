from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import homepage

class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        self.assertEqual(resolve('/').func, homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do</title>', html)
        self.assertTrue(html.endswith('</html>'))


