from django.test import SimpleTestCase
from django.http import HttpResponse


class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        
    def test_response_error_handler(self):
        return HttpResponse('Error handler content', status=403)
        
