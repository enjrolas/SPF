# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Command.quantity'
        db.add_column('command_command', 'quantity',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Command.quantity'
        db.delete_column('command_command', 'quantity')


    models = {
        'command.command': {
            'Meta': {'object_name': 'Command'},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'commandTimeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'parameter': ('django.db.models.fields.FloatField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'statusTimeStamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['command']