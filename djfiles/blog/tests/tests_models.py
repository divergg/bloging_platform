import os
from django.test import TestCase
from blog.models import Record, Image, Avatar
from django.core.files.uploadedfile import SimpleUploadedFile



class RecordModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        Record.objects.create(
            title='Название',
            contents='some_text',
        )

    def __test_label(self, field: str, checked_name: str):
        record = Record.objects.get(id=1)
        label = record._meta.get_field(field).verbose_name
        self.assertEqual(label, checked_name)

    def test_user_label(self):
        self.__test_label('user', 'Автор')

    def test_title_label(self):
        self.__test_label('title', 'Название')

    def test_contents_label(self):
        self.__test_label('contents', 'Содержание')


class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Image.objects.create(
            image=SimpleUploadedFile(name='test_image.png', content=open('blog/tests/test_image.PNG', 'rb').read(), ),
        )

    def test_image_location(self):
        image = Image.objects.get(id=1)
        location = image._meta.get_field('image').upload_to
        MEDIA_URL = '/media/'
        self.assertEqual(MEDIA_URL + location, '/media/images/')

    def test_image_label(self):
        image = Image.objects.get(id=1)
        label = image._meta.get_field('image').verbose_name
        checked_name = 'Изображение'
        self.assertEqual(label, checked_name)


class AvatarModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Avatar.objects.create(
            avat=SimpleUploadedFile(name='test_avatar.png', content=open('blog/tests/test_avatar.PNG', 'rb').read(), ),
        )

    def test_avatar_location(self):
        avatar = Avatar.objects.get(id=1)
        location = avatar._meta.get_field('avat').upload_to
        MEDIA_URL = '/media/'
        self.assertEqual(MEDIA_URL + location, '/media/avatars/')

    def test_avatar_label(self):
        avatar = Avatar.objects.get(id=1)
        label = avatar._meta.get_field('avat').verbose_name
        checked_name = 'Аватар'
        self.assertEqual(label, checked_name)

