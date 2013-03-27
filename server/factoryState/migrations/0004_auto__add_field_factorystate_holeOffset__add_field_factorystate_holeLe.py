# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FactoryState.holeOffset'
        db.add_column('factoryState_factorystate', 'holeOffset',
                      self.gf('django.db.models.fields.FloatField')(default=5.1799999999999997),
                      keep_default=False)

        # Adding field 'FactoryState.holeLength'
        db.add_column('factoryState_factorystate', 'holeLength',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'FactoryState.padLength'
        db.add_column('factoryState_factorystate', 'padLength',
                      self.gf('django.db.models.fields.FloatField')(default=3),
                      keep_default=False)

        # Adding field 'FactoryState.tabbingConnection'
        db.add_column('factoryState_factorystate', 'tabbingConnection',
                      self.gf('django.db.models.fields.FloatField')(default=18),
                      keep_default=False)

        # Adding field 'FactoryState.tabbingOffset'
        db.add_column('factoryState_factorystate', 'tabbingOffset',
                      self.gf('django.db.models.fields.FloatField')(default=20.5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FactoryState.holeOffset'
        db.delete_column('factoryState_factorystate', 'holeOffset')

        # Deleting field 'FactoryState.holeLength'
        db.delete_column('factoryState_factorystate', 'holeLength')

        # Deleting field 'FactoryState.padLength'
        db.delete_column('factoryState_factorystate', 'padLength')

        # Deleting field 'FactoryState.tabbingConnection'
        db.delete_column('factoryState_factorystate', 'tabbingConnection')

        # Deleting field 'FactoryState.tabbingOffset'
        db.delete_column('factoryState_factorystate', 'tabbingOffset')


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
            'conveyorPosition': ('django.db.models.fields.FloatField', [], {}),
            'encapsulantInTub': ('django.db.models.fields.IntegerField', [], {}),
            'holeLength': ('django.db.models.fields.FloatField', [], {}),
            'holeOffset': ('django.db.models.fields.FloatField', [], {}),
            'hopperPosition': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'padLength': ('django.db.models.fields.FloatField', [], {}),
            'soletteLength': ('django.db.models.fields.FloatField', [], {}),
            'soletteSpacing': ('django.db.models.fields.FloatField', [], {}),
            'soletteWidth': ('django.db.models.fields.FloatField', [], {}),
            'solettesInHopper': ('django.db.models.fields.IntegerField', [], {}),
            'suctionDelay': ('django.db.models.fields.IntegerField', [], {}),
            'suctionReleaseTime': ('django.db.models.fields.IntegerField', [], {}),
            'tabbingConnection': ('django.db.models.fields.FloatField', [], {}),
            'tabbingLength': ('django.db.models.fields.FloatField', [], {}),
            'tabbingOffset': ('django.db.models.fields.FloatField', [], {}),
            'tabbingOnSpool': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['factoryState']