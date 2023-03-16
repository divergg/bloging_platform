from django.contrib import admin

# Register your models here.
from blog.models import Record, Image, Avatar

class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['title', 'contents', 'user']
    list_filter = ['title']
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'record']
    list_filter = ['record']

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ['avat', 'user']



