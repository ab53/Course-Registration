from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
		login,
		logout,
		logout_then_login,
	) 

urlpatterns = [

	url(r'^login/$',login,name='login'),
	url(r'^logout/$',logout,{'template_name': 'account/logged_out.html'},name='logout'),
	url(r'^logout-then-login/$',logout_then_login,name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^register/$', views.register, name='register'),
	url(r'^add/$', views.add_course, name='add'),
	url(r'^(?P<id>[0-9]+)/new/$', views.new_course, name='new'),
	url(r'^status/$', views.status_course, name='status'),
	url(r'^(?P<id>[0-9]+)/detail/$', views.detail, name='detail'),
]