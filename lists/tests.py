
from django.urls import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpResponse

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpResponse()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected_html)
