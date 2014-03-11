# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MatchEvaluation'
        db.create_table(u'sony_tv_matchevaluation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('episode_query', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sony_tv.EpisodeQuery'])),
            ('wiki_id', self.gf('django.db.models.fields.IntegerField')()),
            ('page_id', self.gf('django.db.models.fields.IntegerField')()),
            ('wrong_wiki', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wrong_episode', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sony_tv', ['MatchEvaluation'])


    def backwards(self, orm):
        # Deleting model 'MatchEvaluation'
        db.delete_table(u'sony_tv_matchevaluation')


    models = {
        u'sony_tv.episodequery': {
            'Meta': {'object_name': 'EpisodeQuery'},
            'comments': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'expected_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sony_tv.matchevaluation': {
            'Meta': {'object_name': 'MatchEvaluation'},
            'comments': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode_query': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sony_tv.EpisodeQuery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'wiki_id': ('django.db.models.fields.IntegerField', [], {}),
            'wrong_episode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wrong_wiki': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'sony_tv.result': {
            'Meta': {'object_name': 'Result'},
            'article_quality': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'content_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sony_tv.EpisodeQuery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'raw_response': ('django.db.models.fields.TextField', [], {}),
            'run': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sony_tv.Run']"}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'wiki_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'})
        },
        u'sony_tv.run': {
            'Meta': {'object_name': 'Run'},
            'comments': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sony_tv']