from django import forms
from blog.models import User, Record
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class AuthForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Password')


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, label=_('First name'))
    last_name = forms.CharField(max_length=50, required=True, label=_('Last name'))
    email = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class RecordCreateForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = '__all__'
        exclude = ['user', 'date_of_creation']


class AvatarUploadForm(forms.Form):
    image = forms.ImageField(label=_('UserPic'), required=False)


class ImageAddForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label=_('Image'))




class RecordUploadForm(forms.Form):
    file = forms.FileField(
        label=_('file')
    )





