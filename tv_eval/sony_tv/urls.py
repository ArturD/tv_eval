from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', 'sony_tv.views.run_list'),
)
