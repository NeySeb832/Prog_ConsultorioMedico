from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


class MainpageViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func, views.home)

    def test_about_view_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_url_resolves(self):
        resolver = resolve('/about/')
        self.assertEqual(resolver.func, views.about)

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_url_resolves(self):
        resolver = resolve('/contact/')
        self.assertEqual(resolver.func, views.contact)
