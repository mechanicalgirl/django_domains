from django.conf.urls.defaults import *
from django.contrib import admin

from django_domains.admin import site

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', site.root),
    (r'^(.*)$', site.root),
)
