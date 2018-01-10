from django.test import TestCase


class ContactPageTest(TestCase):

    def test_contact_page_renders_contact_template(self):
        response = self.client.get('/contact/')

        self.assertTemplateUsed(response, 'contact/contact.html')
