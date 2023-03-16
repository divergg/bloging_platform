from django.urls import path, include
from blog.views import RecordListView, SiteLogoutView, SiteLoginView, RegisterView, RecordCreateView, RecordDetailView, RecordUploadView, AccountInfoView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', RecordListView.as_view(), name='records_list'),
    path('<int:pk>', RecordDetailView.as_view(), name='record_detail'),
    path('login', SiteLoginView.as_view(), name='login'),
    path('logout', SiteLogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('account', AccountInfoView.as_view(), name='account'),
    path('record_create', RecordCreateView.as_view(), name='record_create'),
    path('record_file_upload', RecordUploadView.as_view(), name='record_upload'),
    path('i18n/', include('django.conf.urls.i18n'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
