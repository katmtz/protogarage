# Build18 Garage Prototype URLS

from django.conf.urls import patterns,include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'garage.views.home', name='home'),
	url(r'^login/$','garage.views.login', name="login"),
	url(r'^signup/$','garage.views.signup', name="signup"),
	)