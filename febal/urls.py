from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'febal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^informes/tickets/$', 'informes.views.informeTickets'),    
    
)
