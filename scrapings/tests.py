from django.test import TestCase
from django.urls import reverse


class ScrapingTemplatesTest(TestCase):
    """A class testing the Scrapings templates"""

    def test_citizen_home_template(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_home_page_url_name(self):
        res = self.client.get(reverse('scrapings:citizen'))
        self.assertEqual(res.status_code, 200)
        
    def test_home_template_user(self):
        res = self.client.get('/')
        self.assertTemplateUsed(res, 'citizen/index.html')

    def test_home_page_template_contains_correct_html(self):
        res = self.client.get('/')
        self.assertContains(res, 'Welcome')

    def test_home_page_template_does_not_contains_incorrect_hmtl(self):
        res = self.client.get('/')
        self.assertNotContains(res, 'not on the template html')


