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

    url(r'^admin/', include(admin.site.urls)),
)
