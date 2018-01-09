from django.test import TestCase
from django.urls import resolve
from django.http import HttpResponse, HttpRequest

from .views import home_page


class HomePageTests(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home/home.html')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Home | JonnyJE Technical Support</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    # def test_home_page_displays_correct_h1_header(self):
    #

    def test_home_page_extends_base_html_and_displays_header(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        expected_header = 'JonnyJE Technical Support'

        self.assertIn(expected_header, html)
