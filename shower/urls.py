from django.conf.urls import url
from django.contrib import admin
from .views import RegistryListView, RegistryItemCompletedView

urlpatterns = [
    url(r'^$', RegistryListView.as_view(), name='registry'),
    url(r'^(?P<pk>[0-9]+)/$', RegistryItemCompletedView.as_view(), name='mark-purchased'),
]
