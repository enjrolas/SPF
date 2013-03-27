# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FactoryState.tabbingLength'
        db.add_column('factoryState_factorystate', 'tabbingLength',
                      self.gf('django.db.models.fields.FloatField')(default=20),
                      keep_default=False)

        # Adding field 'FactoryState.hopperPosition'
        db.add_column('factoryState_factorystate', 'hopperPosition',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState.conveyorPosition'
        db.add_column('factoryState_factorystate', 'conveyorPosition',
                      self.gf('django.db.models.fields.FloatField')(default=400),
                      keep_default=False)

        # Adding field 'FactoryState.suctionReleaseTime'
        db.add_column('factoryState_factorystate', 'suctionReleaseTime',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.suctionDelay'
        db.add_column('factoryState_factorystate', 'suctionDelay',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FactoryState.tabbingLength'
        db.delete_column('factoryState_factorystate', 'tabbingLength')

        # Deleting field 'FactoryState.hopperPosition'
        db.delete_column('factoryState_factorystate', 'hopperPosition')

        # Deleting field 'FactoryState.conveyorPosition'
        db.delete_column('factoryState_factorystate', 'conveyorPosition')

        # Deleting field 'FactoryState.suctionReleaseTime'
        db.delete_column('factoryState_factorystate', 'suctionReleaseTime')

        # Deleting field 'FactoryState.suctionDelay'
        db.delete_column('factoryState_factorystate', 'suctionDelay')


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
            'hopperPosition': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soletteLength': ('django.db.models.fields.FloatField', [], {}),
            'soletteSpacing': ('django.db.models.fields.FloatField', [], {}),
            'soletteWidth': ('django.db.models.fields.FloatField', [], {}),
            'solettesInHopper': ('django.db.models.fields.IntegerField', [], {}),
            'suctionDelay': ('django.db.models.fields.IntegerField', [], {}),
            'suctionReleaseTime': ('django.db.models.fields.IntegerField', [], {}),
            'tabbingLength': ('django.db.models.fields.FloatField', [], {}),
            'tabbingOnSpool': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['factoryState']