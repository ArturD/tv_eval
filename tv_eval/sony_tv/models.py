# -*- coding: utf-8 -*-
import json
import requests
from django.db import models

TYPE_CHOICES = (
      ('te','tv_episode'),
      ('ts','tv_season'),
      ('','don\'t know'),
    )

class ModelBase(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  comments = models.TextField(blank=True, default='')

  class Meta:
    abstract = True

class EpisodeQuery(ModelBase):
  series_name = models.CharField(max_length=100)
  episode_title = models.CharField(max_length=100)
  expected_type = models.CharField(max_length=2, blank=True, default='', choices=TYPE_CHOICES)

  def run(self, run):
    r = requests.get(run.url, params={"seriesName": self.series_name, "episodeName": self.episode_title})
    if r.status_code == 200:
      m = r.json()
      result = Result(run=run, episode=self, wiki_id=m['wikiId'], page_id=m['articleId'], title=m['title'], url=m['url'], content_url=m['contentUrl'], raw_response=r.text, success=True)
      result.save()
    else:
      result = Result(run=run, episode=self,raw_response=r.text)
      result.save()

  def __str__(self):
    return "%s: %s" % (self.series_name, self.episode_title)

class Run(ModelBase):
  url = models.CharField(max_length=100)

  def run(self):
    for eq in EpisodeQuery.objects.all():
      eq.run(self)

  def get_absolute_url(self):
    from django.core.urlresolvers import reverse
    return reverse('sony_tv.views.run_details', args=[str(self.id)])

  def __unicode__(self):
    return u'%s, %s' % (self.created_at, self.url)

  def compute_stats(self):
    stats = {}
    results = self.result_set.all()
    stats['all'] = len(results)
    stats['all_percent'] = 100
    stats['has_result'] = len([x for x in results if x.success])
    stats['has_result_percent'] = round(100.0 * stats['has_result'] / stats['all'], 2)
    return stats

  def get_stats(self):
    from django.core.cache import cache
    key = ('run_stats_%d' % self.pk)
    #stats = cache.get(key)
    stats = None
    if stats == None:
      stats = self.compute_stats()
      cache.set(key, stats)
    return stats

  def stats_all(self):
    return self.get_stats()['all']

  def stats_all_percent(self):
    return self.get_stats()['all_percent']

  def stats_has_result(self):
    return self.get_stats()['has_result']

  def stats_has_result_percent(self):
    return self.get_stats()['has_result_percent']

class Result(ModelBase):
  episode = models.ForeignKey(EpisodeQuery)
  run = models.ForeignKey(Run)

  success = models.BooleanField(default=False)

  wiki_id = models.IntegerField(null=True, default=None)
  page_id = models.IntegerField(null=True, default=None)
  title = models.CharField(max_length=50, blank=True, default='')
  url = models.CharField(max_length=256, blank=True, default='')
  content_url = models.CharField(max_length=256, blank=True, default='')
  raw_response = models.TextField()

  def __unicode__(self):
    if self.success:
      return u'%s: %s' % (self.episode, self.url)
    else:
      return u'%s: FAIL' % self.episode


