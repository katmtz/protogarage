# Build18 Garage Prototype URLS

from django.conf.urls import patterns,include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'garage.views.home', name='home'),
	url(r'^login/$','garage.views.signin', name="login"),
	url(r'^logout/$','garage.views.signout',name="logout"),
	url(r'^signup/$','garage.views.signup', name="signup"),
	url(r'^usercreate/$','garage.views.create_user',name="create_user"),
	url(r'^authenticator/$', 'garage.views.authenticator', name='authenticator'),
	url(r'^admin/', include(admin.site.urls)),
	)