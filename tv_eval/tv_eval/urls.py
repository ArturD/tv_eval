from django.conf.urls import patterns, include, url

from django.contrib import admin
import sony_tv.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tv_eval.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(sony_tv.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
