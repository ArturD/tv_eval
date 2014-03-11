from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', 'sony_tv.views.run_list'),
  url(r'^run/(\d+)$', 'sony_tv.views.run_details'),
  url(r'^evalutions/(\d+)$', 'sony_tv.views.evaluate_result'),
)
