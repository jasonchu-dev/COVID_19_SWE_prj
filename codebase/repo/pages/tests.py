from django.test import SimpleTestCase
from django.http import HttpResponse
import views



class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        print('Testing landing page:    Expected= 200')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        print('Testing about page:      Expected= 200')
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
     def test_delete_page_status_code(self):
        print('Testing delete page:      Expected= 200')
        response = self.client.get('/delete/')
        self.assertEqual(response.status_code, 200)
        
     def test_insert_page_status_code(self):
        print('Testing insert page:      Expected= 200')
        response = self.client.get('/insert/')
        self.assertEqual(response.status_code, 200)
     
     def test_analytics_page_status_code(self):
        print('Testing analytics page:      Expected= 200')
        response = self.client.get('/analytics/')
        self.assertEqual(response.status_code, 200)
    
    def test_response_error_handler(self):
        print('Testing error response:  Expected= 403 ')
        return HttpResponse('Error handler content', status=403)
    
#class ViewsTests(SimpleTestCase):
#    def test_insert_record_category(self):
#       print('Testing insert record category field:  Expected= ??')       
#     
#   def test_edit_record_ID(self):
#        print('Testing input ID field: Expected=2')
#        input = views.modify_record.get(recordID = 2)
#        self.assertEqual(input, 2)
        
