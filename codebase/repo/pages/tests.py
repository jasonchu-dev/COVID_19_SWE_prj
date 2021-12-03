from django.test import SimpleTestCase
from django.http import HttpResponse


class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        print('Testing landing page:    Expected= 200')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        print('Testing /about page:      Expected= 200')
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    """ def test_search_page_status_code(self):
        print('Testing /search page:    Expected= 200')
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200) """

    def test_delete_page_status_code(self):
       print('Testing /delete page:      Expected= 200')
       response = self.client.get('/delete/')
       self.assertEqual(response.status_code, 200)

    """ def test_delete_record_code(self):
       print('Testing delete record:      Expected= 200')
       response = self.client.get('/delete/delete')
       self.assertEqual(response.status_code, 200) """
        
    def test_insert_page_status_code(self):
       print('Testing /insert page:      Expected= 200')
       response = self.client.get('/insert/')
       self.assertEqual(response.status_code, 200)
    
    """ def test_insert_record_code(self):
       print('Testing insert record:      Expected= 200')
       response = self.client.get('/insert/insert')
       self.assertEqual(response.status_code, 200) """

    """ def test_modify_record_code(self):
       print('Testing modify record:      Expected= 200')
       response = self.client.get('/insert/modify')
       self.assertEqual(response.status_code, 200) """
     
    def test_backup_button_code(self):
       print('Testing /backup records:      Expected= 200')
       response = self.client.get('/backup/')
       self.assertEqual(response.status_code, 200)
    
    #testing analytics page
    def test_analytics_page_status_code(self):
       print('Testing /analytics page:      Expected= 200')
       response = self.client.get('/analytics/')
       self.assertEqual(response.status_code, 200)

    """ def test_analytics_monthlyVaccs_status_code(self):
       print('Testing /analytics/monthlyVaccs page:      Expected= 200')
       response = self.client.get('/analytics/monthlyVaccs')
       self.assertEqual(response.status_code, 200) """

    def test_race_vaccine_analytics_status_code(self):
       print('Testing /analytics/race page:      Expected= 200')
       response = self.client.get('/analytics/race')
       self.assertEqual(response.status_code, 200)
    
    def test_gender_analytics_status_code(self):
       print('Testing /analytics/gender page:      Expected= 200')
       response = self.client.get('/analytics/gender')
       self.assertEqual(response.status_code, 200)

    def test_fullyVacc_analytics_status_code(self):
       print('Testing /analytics/fullyVacc page:      Expected= 200')
       response = self.client.get('/analytics/fullyVacc')
       self.assertEqual(response.status_code, 200)

    def test_ageGroup_analytics_status_code(self):
       print('Testing /analytics/age page:      Expected= 200')
       response = self.client.get('/analytics/age')
       self.assertEqual(response.status_code, 200)
    
    def test_race_vaccine_analytics_status_code(self):
       print('Testing /analytics/brand page:      Expected= 200')
       response = self.client.get('/analytics/brand')
       self.assertEqual(response.status_code, 200)
    
    def test_analytics2_page_status_code(self):
       print('Testing /analytics/analytics2 page:      Expected= 200')
       response = self.client.get('/analytics/analytics2')
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
    

    