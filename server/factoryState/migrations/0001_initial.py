# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FactoryState'
        db.create_table('factoryState_factorystate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_1ma', self.gf('django.db.models.fields.IntegerField')()),
            ('_2ma', self.gf('django.db.models.fields.IntegerField')()),
            ('_3ma', self.gf('django.db.models.fields.IntegerField')()),
            ('_4ma', self.gf('django.db.models.fields.IntegerField')()),
            ('_xfr', self.gf('django.db.models.fields.IntegerField')()),
            ('_yfr', self.gf('django.db.models.fields.IntegerField')()),
            ('_zfr', self.gf('django.db.models.fields.IntegerField')()),
            ('_afr', self.gf('django.db.models.fields.IntegerField')()),
            ('_xvm', self.gf('django.db.models.fields.IntegerField')()),
            ('_yvm', self.gf('django.db.models.fields.IntegerField')()),
            ('_zvm', self.gf('django.db.models.fields.IntegerField')()),
            ('_avm', self.gf('django.db.models.fields.IntegerField')()),
            ('_xtr', self.gf('django.db.models.fields.FloatField')()),
            ('_ytr', self.gf('django.db.models.fields.FloatField')()),
            ('_ztr', self.gf('django.db.models.fields.FloatField')()),
            ('_atr', self.gf('django.db.models.fields.FloatField')()),
            ('_xsa', self.gf('django.db.models.fields.FloatField')()),
            ('_ysa', self.gf('django.db.models.fields.FloatField')()),
            ('_zsa', self.gf('django.db.models.fields.FloatField')()),
            ('_asa', self.gf('django.db.models.fields.FloatField')()),
            ('_1pm', self.gf('django.db.models.fields.IntegerField')()),
            ('_2pm', self.gf('django.db.models.fields.IntegerField')()),
            ('_3pm', self.gf('django.db.models.fields.IntegerField')()),
            ('_4pm', self.gf('django.db.models.fields.IntegerField')()),
            ('solettesInHopper', self.gf('django.db.models.fields.IntegerField')()),
            ('tabbingOnSpool', self.gf('django.db.models.fields.IntegerField')()),
            ('backingsInHopper', self.gf('django.db.models.fields.IntegerField')()),
            ('encapsulantInTub', self.gf('django.db.models.fields.IntegerField')()),
            ('backingWidth', self.gf('django.db.models.fields.FloatField')()),
            ('backingLength', self.gf('django.db.models.fields.FloatField')()),
            ('soletteWidth', self.gf('django.db.models.fields.FloatField')()),
            ('soletteLength', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('factoryState', ['FactoryState'])


    def backwards(self, orm):
        # Deleting model 'FactoryState'
        db.delete_table('factoryState_factorystate')


    models = {
        'factoryState.factorystate': {
            'Meta': {'object_name': 'FactoryState'},
            '_1ma': ('django.db.models.fields.IntegerField', [], {}),
            '_1pm': ('django.db.models.fields.IntegerField', [], {}),
            '_2ma': ('django.db.models.fields.IntegerField', [], {}),
            '_2pm': ('django.db.models.fields.IntegerField', [], {}),
            '_3ma': ('django.db.models.fields.IntegerField', [], {}),
            '_3pm': ('django.db.models.fields.IntegerField', [], {}),
            '_4ma': ('django.db.models.fields.IntegerField', [], {}),
            '_4pm': ('django.db.models.fields.IntegerField', [], {}),
            '_afr': ('django.db.models.fields.IntegerField', [], {}),
            '_asa': ('django.db.models.fields.FloatField', [], {}),
            '_atr': ('django.db.models.fields.FloatField', [], {}),
            '_avm': ('django.db.models.fields.IntegerField', [], {}),
            '_xfr': ('django.db.models.fields.IntegerField', [], {}),
            '_xsa': ('django.db.models.fields.FloatField', [], {}),
            '_xtr': ('django.db.models.fields.FloatField', [], {}),
            '_xvm': ('django.db.models.fields.IntegerField', [], {}),
            '_yfr': ('django.db.models.fields.IntegerField', [], {}),
            '_ysa': ('django.db.models.fields.FloatField', [], {}),
            '_ytr': ('django.db.models.fields.FloatField', [], {}),
            '_yvm': ('django.db.models.fields.IntegerField', [], {}),
            '_zfr': ('django.db.models.fields.IntegerField', [], {}),
            '_zsa': ('django.db.models.fields.FloatField', [], {}),
            '_ztr': ('django.db.models.fields.FloatField', [], {}),
            '_zvm': ('django.db.models.fields.IntegerField', [], {}),
            'backingLength': ('django.db.models.fields.FloatField', [], {}),
            'backingWidth': ('django.db.models.fields.FloatField', [], {}),
            'backingsInHopper': ('django.db.models.fields.IntegerField', [], {}),
            'encapsulantInTub': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soletteLength': ('django.db.models.fields.FloatField', [], {}),
            'soletteWidth': ('django.db.models.fields.FloatField', [], {}),
            'solettesInHopper': ('django.db.models.fields.IntegerField', [], {}),
            'tabbingOnSpool': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['factoryState']