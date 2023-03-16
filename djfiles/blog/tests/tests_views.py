from django.test import TestCase
from blog.urls import urlpatterns
from django.urls import reverse
from blog.models import Record, User


PROJECT_URLS = [url.pattern.name for url in urlpatterns]
NUMBER_OF_RECORDS = 10

class TemplateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for index in range(NUMBER_OF_RECORDS):
            Record.objects.create(
                title=f'Название {index}',
                contents='some_text',
            )



    def test_templates_exist(self):
        self.client.login(username='test', password='testpassword')
        for url in PROJECT_URLS:
            if 'detail' in url:
                arg_list = [record.id for record in Record.objects.all()]
                for arg in arg_list:
                    response = self.client.get(reverse(url, args=[arg]))
                    self.assertFalse(response.status_code == 404)
            else:
                response = self.client.get(reverse(url))
                self.assertFalse(response.status_code == 404)

    def test_main_page(self):
        url = 'records_list'
        response = self.client.get(reverse(url))
        record_quantity = len(response.context['records_list'])
        self.assertEqual(record_quantity, NUMBER_OF_RECORDS)




class AccessDeniedTest(TestCase):

    URLS = ['account', 'record_create', 'record_upload']

    def test_access(self):
        for url in self.URLS:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 403)



#




