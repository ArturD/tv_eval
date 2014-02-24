# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EpisodeQuery'
        db.create_table(u'sony_tv_episodequery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('series_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('episode_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('expected_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=2, null=True)),
        ))
        db.send_create_signal(u'sony_tv', ['EpisodeQuery'])

        # Adding model 'Run'
        db.create_table(u'sony_tv_run', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sony_tv', ['Run'])

        # Adding model 'Result'
        db.create_table(u'sony_tv_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sony_tv.EpisodeQuery'])),
            ('run', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sony_tv.Run'])),
            ('wiki_id', self.gf('django.db.models.fields.IntegerField')()),
            ('page_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('raw_response', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sony_tv', ['Result'])


    def backwards(self, orm):
        # Deleting model 'EpisodeQuery'
        db.delete_table(u'sony_tv_episodequery')

        # Deleting model 'Run'
        db.delete_table(u'sony_tv_run')

        # Deleting model 'Result'
        db.delete_table(u'sony_tv_result')


    models = {
        u'sony_tv.episodequery': {
            'Meta': {'object_name': 'EpisodeQuery'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'expected_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sony_tv.result': {
            'Meta': {'object_name': 'Result'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'content_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sony_tv.EpisodeQuery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {}),
            'raw_response': ('django.db.models.fields.TextField', [], {}),
            'run': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sony_tv.Run']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'wiki_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'sony_tv.run': {
            'Meta': {'object_name': 'Run'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sony_tv']