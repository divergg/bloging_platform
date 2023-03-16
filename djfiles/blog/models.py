from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Record(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, related_name='Автор',
                             verbose_name=_('author'))
    title = models.TextField(max_length=100, verbose_name=_('title'))
    contents = models.TextField(default=None, verbose_name=_('contents'))
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name=_('date of creation'))


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('records')
        verbose_name = _('record')


class Image(models.Model):
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True, verbose_name=_('image'))
    record = models.ForeignKey(Record, default=None, null=True, on_delete=models.CASCADE, related_name='Запись',
                             verbose_name=_('record'))

    class Meta:
        verbose_name_plural = _('images')
        verbose_name = _('image')


class Avatar(models.Model):
    avat = models.ImageField(upload_to='avatars/', default=None, blank=True, null=True, verbose_name=_('userPic'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'), blank=True, null=True)

    class Meta:
        verbose_name_plural = _('avatars')
        verbose_name = _('avatar')











