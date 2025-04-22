from django.test import TestCase
from django.urls import resolve

from .views import homepage

class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        self.assertEqual(resolve('/').func, homepage)
