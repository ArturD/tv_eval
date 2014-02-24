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
      try:
        result.article_quality = get_article_quality(m['wikiId'], m['articleId'])
      except:
        pass
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
    if len(results) > 0:
      stats['all'] = len(results)
      stats['all_percent'] = 100
      stats['has_result'] = len([x for x in results if x.success])
      stats['has_result_percent'] = round(100.0 * stats['has_result'] / stats['all'], 2)
    else:
      stats['all'] = '-'
      stats['all_percent'] = '-'
      stats['has_result'] = '-'
      stats['has_result_percent'] = '-'
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

  def stats_article_quality(self):
    results = self.result_set.filter(success=True).all()
    stats = {}
    if len(results) > 0:
      for lb in [50, 75, 90, 95, 99]:
        count = len([x for x in results if lb <= x.article_quality])
        stats[lb] = (count, 100.0 * count / len(results))
    return sorted(stats.items())


class Result(ModelBase):
  episode = models.ForeignKey(EpisodeQuery)
  run = models.ForeignKey(Run)

  success = models.BooleanField(default=False)

  article_quality = models.IntegerField(null=True, default=None)
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

def get_article_quality(wid, pid):
  root_url = 'http://search-s10:8983/solr/main/select'
  params = {'q': 'id:%s_%s' % (wid, pid), 'fl': 'article_quality_i', 'wt': 'json' }
  resp = requests.get(root_url, params=params)
  if resp.status_code == 200:
    m = resp.json()
    if m['response'] and m['response']['docs'] and m['response']['docs'][0]:
      return m['response']['docs'][0]['article_quality_i']
  return None

