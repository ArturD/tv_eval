from django.db import models

TYPE_CHOICES = (
      ('te','tv_episode'),
      ('ts','tv_season'),
      (None,'don\'t know'),
    ),

class ModelBase(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  comments = models.TextField()

  class Meta:
    abstract = True

class EpisodeQuery(ModelBase):
  series_name = models.CharField(max_length=100)
  episode_title = models.CharField(max_length=100)
  expected_type = models.CharField(max_length=2, null=True, default=None)

class Run(ModelBase):
  url = models.CharField(max_length=100)

class Result(ModelBase):
  episode = models.ForeignKey(EpisodeQuery)
  run = models.ForeignKey(Run)

  wiki_id = models.IntegerField()
  page_id = models.IntegerField()
  title = models.CharField(max_length=50)
  url = models.CharField(max_length=256)
  content_url = models.CharField(max_length=256)
  raw_response = models.TextField()
