# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Result.success'
        db.add_column(u'sony_tv_result', 'success',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Result.wiki_id'
        db.alter_column(u'sony_tv_result', 'wiki_id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Result.page_id'
        db.alter_column(u'sony_tv_result', 'page_id', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Result.success'
        db.delete_column(u'sony_tv_result', 'success')


        # User chose to not deal with backwards NULL issues for 'Result.wiki_id'
        raise RuntimeError("Cannot reverse this migration. 'Result.wiki_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Result.wiki_id'
        db.alter_column(u'sony_tv_result', 'wiki_id', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Result.page_id'
        raise RuntimeError("Cannot reverse this migration. 'Result.page_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Result.page_id'
        db.alter_column(u'sony_tv_result', 'page_id', self.gf('django.db.models.fields.IntegerField')())

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
        u'sony_tv.result': {
            'Meta': {'object_name': 'Result'},
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