from django.conf.urls import patterns, include, url
from djangotestsite.views import hello
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotestsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', hello),
)
