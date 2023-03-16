from django.shortcuts import render

# Create your views here.
from django.views import View, generic
from blog.models import Record, Image, Avatar
from django.contrib.auth.views import LoginView, LogoutView
from blog.forms import RegisterForm, RecordCreateForm, ImageAddForm, RecordUploadForm, UserUpdateForm, AvatarUploadForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from csv import reader
from django.utils.translation import gettext as _



class RecordListView(generic.ListView):
    model = Record
    template_name = 'blog/records_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records_list'] = Record.objects.all().order_by('-date_of_creation')
        return context


class RecordDetailView(generic.DetailView):
    model = Record
    template_name = 'blog/record_detail.html'
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(record=self.get_object())
        return context

class RecordCreateView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        form_rec = RecordCreateForm()
        form_im = ImageAddForm()
        return render(request, 'blog/record_create.html', context={'form_rec': form_rec, 'form_im': form_im})


    def post(self, request):
        form_rec = RecordCreateForm(request.POST)
        form_im = ImageAddForm(request.POST, request.FILES)
        if form_rec.is_valid() and form_im.is_valid():
            rec = form_rec.save()
            rec.user = request.user
            rec.save()
            images = request.FILES.getlist('image')
            for ims in images:
                image = Image.objects.create(image=ims, record=rec)
                image.save()
            return HttpResponseRedirect('/')
        return render(request, 'blog/record_create.html', context={'form_rec': form_rec, 'form_im': form_im})


class RecordUploadView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        form = RecordUploadForm
        return render(request, 'blog/record_file_upload.html', context={'form': form})

    def post(self, request):
        form = RecordUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file'].read()
            record_str = file.decode('windows-1251').split('\n')
            csv_reader = reader(record_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                if row == []:
                    break
                string = row[0].split(';')
                rec = Record.objects.create(
                    user=request.user,
                    title=string[0],
                    contents=string[1]
                )
                rec.save()
            return HttpResponseRedirect('/')
        return render(request, 'blog/record_file_upload.html', context={'form': form})

class SiteLoginView(LoginView):
    template_name = 'blog/login.html'


class SiteLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'blog/register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pass_w = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pass_w)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'blog/register.html', context={'form': form})


class AccountInfoView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        user = request.user
        form_user = UserUpdateForm(instance=user)
        if Avatar.objects.filter(user=user):
            avatar = Avatar.objects.get(user=user)
        else:
            avatar = None
        form_avatar = AvatarUploadForm()
        return render(request, 'blog/account.html', context={'user': user, 'form_user': form_user, 'form_avatar': form_avatar, 'avatar': avatar})

    def post(self, request):
        user = request.user
        form_user = UserUpdateForm(request.POST, instance=user)
        form_avatar = AvatarUploadForm(request.POST, request.FILES)
        if form_user.is_valid() and form_avatar.is_valid():
            form_user.save()
            if Avatar.objects.filter(user=user):
                avat = Avatar.objects.get(user=user)
                avat.delete()
            image = request.FILES.get('image')
            avat = Avatar.objects.create(avat=image, user=user)
            avat.save()
            return HttpResponseRedirect('/account')
        return render(request, 'blog/account.html',
                      context={'user': user, 'form_user': form_user, 'form_avatar': form_avatar})




