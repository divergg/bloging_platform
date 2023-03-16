from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import User


class FormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test', password='testpassword')

    def test_avatar_upload_data(self):
        self.client.login(username='test', password='testpassword')
        template = 'account'
        url = reverse(template)
        response = self.client.post(url, data={'image': SimpleUploadedFile(name='test_avatar.png',
                                                                           content=open('blog/tests/test_avatar.PNG', 'rb').read(), )})
        self.assertEqual(response.status_code, 200)

    def test_image_upload_data(self):
        self.client.login(username='test', password='testpassword')
        template = 'record_create'
        url = reverse(template)
        response = self.client.post(url, data={'image': SimpleUploadedFile(name='test_image.png',
                                                                           content=open('blog/tests/test_image.PNG',
                                                                                        'rb').read(), )})
        self.assertEqual(response.status_code, 200)

    def test_file_upload_form(self):
        self.client.login(username='test', password='testpassword')
        template = 'record_upload'
        url = reverse(template)
        response = self.client.post(url, data={'file': SimpleUploadedFile(name='test.csv',
                                                                          content=open('blog/tests/test.csv',
                                                                                        'rb').read(),)})
        self.assertFalse(response.status_code == 404)

