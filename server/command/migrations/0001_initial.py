# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Command'
        db.create_table('command_command', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('commandTimeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parameter', self.gf('django.db.models.fields.FloatField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('statusTimeStamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('json', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('command', ['Command'])


    def backwards(self, orm):
        # Deleting model 'Command'
        db.delete_table('command_command')


    models = {
        'command.command': {
            'Meta': {'object_name': 'Command'},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'commandTimeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'parameter': ('django.db.models.fields.FloatField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'statusTimeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['command']