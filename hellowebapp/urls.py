from collection.backends import MyRegistrationView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
    )


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'collection.views.index', name='home'),
    #url(r'^$', 'collection.views.about', name='about'),
    #url(r'^$', 'collection.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

url(r'^about/$', 
TemplateView.as_view(template_name='about.html'),
 name='about'),

url(r'^contact/$', 
TemplateView.as_view(template_name='contact.html'),
 name='contact'),

url(r'^things/(?P<slug>[-\w]+)/$',
    'collection.views.thing_detail',
    name = 'thing_detail'),
    
#the edit object url

url(r'^things/(?P<slug>[-\w]+)/edit/$',
    'collection.views.edit_thing',
    name='edit_thing'),    
    
#registration



url(r'^accounts/password/reset/$',
    password_reset,
    {'template_name':'registration/password_reset_form.html'},
    name="password_reset"),
    
url(r'^accounts/password/reset/done/$',
    password_reset_done,
    {'template_name':'registration/password_reset_done.html'},
    name="password_reset_done"),  

url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,
    {'template_name':'registration/password_reset_confirm.html'},
    name="password_reset_confirm"),
    
url(r'^accounts/password/done/$',
    password_reset_complete,
    {'template_name':'registration/password_reset_complete.html'},
    name="password_reset_complete"),

url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
url(r'^accounts/create_thing/$', 'collection.views.create_thing', name='registration_create_thing'),


url(r'^accounts/',

include('registration.backends.default.urls')),



  

    url(r'^admin/', include(admin.site.urls)),
)


