from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

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

url(r'^accounts/',

include('registration.backends.simple.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


