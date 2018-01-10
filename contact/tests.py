from django.test import TestCase

from .views import contact_page


class ContactPageTest(TestCase):

    def test_contact_page_renders_contact_template(self):
        response = self.client.get('/contact/')

        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_page_returns_correct_title_and_extends_base(self):
        request = self.client.get('/contact/')
        response = contact_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Contact | JonnyJE Technical Support</title>',
                      html)

    def test_h2_saying_contact_page(self):
        request = self.client.get('/contact/')
        response = contact_page(request)
        html = response.content.decode('utf8')

        self.assertIn('<h2>Contact Page</h2>', html)
