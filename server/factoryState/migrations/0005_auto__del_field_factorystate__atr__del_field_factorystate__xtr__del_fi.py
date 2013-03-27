# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FactoryState._atr'
        db.delete_column('factoryState_factorystate', '_atr')

        # Deleting field 'FactoryState._xtr'
        db.delete_column('factoryState_factorystate', '_xtr')

        # Deleting field 'FactoryState._2pm'
        db.delete_column('factoryState_factorystate', '_2pm')

        # Deleting field 'FactoryState._zsa'
        db.delete_column('factoryState_factorystate', '_zsa')

        # Deleting field 'FactoryState._ytr'
        db.delete_column('factoryState_factorystate', '_ytr')

        # Deleting field 'FactoryState._2ma'
        db.delete_column('factoryState_factorystate', '_2ma')

        # Deleting field 'FactoryState._asa'
        db.delete_column('factoryState_factorystate', '_asa')

        # Deleting field 'FactoryState._ztr'
        db.delete_column('factoryState_factorystate', '_ztr')

        # Deleting field 'FactoryState._ysa'
        db.delete_column('factoryState_factorystate', '_ysa')

        # Deleting field 'FactoryState._afr'
        db.delete_column('factoryState_factorystate', '_afr')

        # Deleting field 'FactoryState._4pm'
        db.delete_column('factoryState_factorystate', '_4pm')

        # Deleting field 'FactoryState._xvm'
        db.delete_column('factoryState_factorystate', '_xvm')

        # Deleting field 'FactoryState._yvm'
        db.delete_column('factoryState_factorystate', '_yvm')

        # Deleting field 'FactoryState._avm'
        db.delete_column('factoryState_factorystate', '_avm')

        # Deleting field 'FactoryState._3pm'
        db.delete_column('factoryState_factorystate', '_3pm')

        # Deleting field 'FactoryState._zfr'
        db.delete_column('factoryState_factorystate', '_zfr')

        # Deleting field 'FactoryState._3ma'
        db.delete_column('factoryState_factorystate', '_3ma')

        # Deleting field 'FactoryState._1ma'
        db.delete_column('factoryState_factorystate', '_1ma')

        # Deleting field 'FactoryState._zvm'
        db.delete_column('factoryState_factorystate', '_zvm')

        # Deleting field 'FactoryState._yfr'
        db.delete_column('factoryState_factorystate', '_yfr')

        # Deleting field 'FactoryState._4ma'
        db.delete_column('factoryState_factorystate', '_4ma')

        # Deleting field 'FactoryState._xfr'
        db.delete_column('factoryState_factorystate', '_xfr')

        # Deleting field 'FactoryState._xsa'
        db.delete_column('factoryState_factorystate', '_xsa')

        # Deleting field 'FactoryState._1pm'
        db.delete_column('factoryState_factorystate', '_1pm')

        # Adding field 'FactoryState.var_1ma'
        db.add_column('factoryState_factorystate', 'var_1ma',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState.var_2ma'
        db.add_column('factoryState_factorystate', 'var_2ma',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FactoryState.var_3ma'
        db.add_column('factoryState_factorystate', 'var_3ma',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Adding field 'FactoryState.var_4ma'
        db.add_column('factoryState_factorystate', 'var_4ma',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)

        # Adding field 'FactoryState.var_xfr'
        db.add_column('factoryState_factorystate', 'var_xfr',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_yfr'
        db.add_column('factoryState_factorystate', 'var_yfr',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_zfr'
        db.add_column('factoryState_factorystate', 'var_zfr',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_afr'
        db.add_column('factoryState_factorystate', 'var_afr',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_xvm'
        db.add_column('factoryState_factorystate', 'var_xvm',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_yvm'
        db.add_column('factoryState_factorystate', 'var_yvm',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_zvm'
        db.add_column('factoryState_factorystate', 'var_zvm',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_avm'
        db.add_column('factoryState_factorystate', 'var_avm',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'FactoryState.var_xtr'
        db.add_column('factoryState_factorystate', 'var_xtr',
                      self.gf('django.db.models.fields.FloatField')(default=122),
                      keep_default=False)

        # Adding field 'FactoryState.var_ytr'
        db.add_column('factoryState_factorystate', 'var_ytr',
                      self.gf('django.db.models.fields.FloatField')(default=75.5),
                      keep_default=False)

        # Adding field 'FactoryState.var_ztr'
        db.add_column('factoryState_factorystate', 'var_ztr',
                      self.gf('django.db.models.fields.FloatField')(default=60.799999999999997),
                      keep_default=False)

        # Adding field 'FactoryState.var_atr'
        db.add_column('factoryState_factorystate', 'var_atr',
                      self.gf('django.db.models.fields.FloatField')(default=10),
                      keep_default=False)

        # Adding field 'FactoryState.var_xsa'
        db.add_column('factoryState_factorystate', 'var_xsa',
                      self.gf('django.db.models.fields.FloatField')(default=0.90000000000000002),
                      keep_default=False)

        # Adding field 'FactoryState.var_ysa'
        db.add_column('factoryState_factorystate', 'var_ysa',
                      self.gf('django.db.models.fields.FloatField')(default=0.90000000000000002),
                      keep_default=False)

        # Adding field 'FactoryState.var_zsa'
        db.add_column('factoryState_factorystate', 'var_zsa',
                      self.gf('django.db.models.fields.FloatField')(default=0.90000000000000002),
                      keep_default=False)

        # Adding field 'FactoryState.var_asa'
        db.add_column('factoryState_factorystate', 'var_asa',
                      self.gf('django.db.models.fields.FloatField')(default=0.90000000000000002),
                      keep_default=False)

        # Adding field 'FactoryState.var_1pm'
        db.add_column('factoryState_factorystate', 'var_1pm',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FactoryState.var_2pm'
        db.add_column('factoryState_factorystate', 'var_2pm',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FactoryState.var_3pm'
        db.add_column('factoryState_factorystate', 'var_3pm',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'FactoryState.var_4pm'
        db.add_column('factoryState_factorystate', 'var_4pm',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FactoryState._atr'
        db.add_column('factoryState_factorystate', '_atr',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._xtr'
        db.add_column('factoryState_factorystate', '_xtr',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._2pm'
        db.add_column('factoryState_factorystate', '_2pm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._zsa'
        db.add_column('factoryState_factorystate', '_zsa',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._ytr'
        db.add_column('factoryState_factorystate', '_ytr',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._2ma'
        db.add_column('factoryState_factorystate', '_2ma',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._asa'
        db.add_column('factoryState_factorystate', '_asa',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._ztr'
        db.add_column('factoryState_factorystate', '_ztr',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._ysa'
        db.add_column('factoryState_factorystate', '_ysa',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._afr'
        db.add_column('factoryState_factorystate', '_afr',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._4pm'
        db.add_column('factoryState_factorystate', '_4pm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._xvm'
        db.add_column('factoryState_factorystate', '_xvm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._yvm'
        db.add_column('factoryState_factorystate', '_yvm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._avm'
        db.add_column('factoryState_factorystate', '_avm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._3pm'
        db.add_column('factoryState_factorystate', '_3pm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._zfr'
        db.add_column('factoryState_factorystate', '_zfr',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._3ma'
        db.add_column('factoryState_factorystate', '_3ma',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._1ma'
        db.add_column('factoryState_factorystate', '_1ma',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._zvm'
        db.add_column('factoryState_factorystate', '_zvm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._yfr'
        db.add_column('factoryState_factorystate', '_yfr',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._4ma'
        db.add_column('factoryState_factorystate', '_4ma',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._xfr'
        db.add_column('factoryState_factorystate', '_xfr',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._xsa'
        db.add_column('factoryState_factorystate', '_xsa',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FactoryState._1pm'
        db.add_column('factoryState_factorystate', '_1pm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'FactoryState.var_1ma'
        db.delete_column('factoryState_factorystate', 'var_1ma')

        # Deleting field 'FactoryState.var_2ma'
        db.delete_column('factoryState_factorystate', 'var_2ma')

        # Deleting field 'FactoryState.var_3ma'
        db.delete_column('factoryState_factorystate', 'var_3ma')

        # Deleting field 'FactoryState.var_4ma'
        db.delete_column('factoryState_factorystate', 'var_4ma')

        # Deleting field 'FactoryState.var_xfr'
        db.delete_column('factoryState_factorystate', 'var_xfr')

        # Deleting field 'FactoryState.var_yfr'
        db.delete_column('factoryState_factorystate', 'var_yfr')

        # Deleting field 'FactoryState.var_zfr'
        db.delete_column('factoryState_factorystate', 'var_zfr')

        # Deleting field 'FactoryState.var_afr'
        db.delete_column('factoryState_factorystate', 'var_afr')

        # Deleting field 'FactoryState.var_xvm'
        db.delete_column('factoryState_factorystate', 'var_xvm')

        # Deleting field 'FactoryState.var_yvm'
        db.delete_column('factoryState_factorystate', 'var_yvm')

        # Deleting field 'FactoryState.var_zvm'
        db.delete_column('factoryState_factorystate', 'var_zvm')

        # Deleting field 'FactoryState.var_avm'
        db.delete_column('factoryState_factorystate', 'var_avm')

        # Deleting field 'FactoryState.var_xtr'
        db.delete_column('factoryState_factorystate', 'var_xtr')

        # Deleting field 'FactoryState.var_ytr'
        db.delete_column('factoryState_factorystate', 'var_ytr')

        # Deleting field 'FactoryState.var_ztr'
        db.delete_column('factoryState_factorystate', 'var_ztr')

        # Deleting field 'FactoryState.var_atr'
        db.delete_column('factoryState_factorystate', 'var_atr')

        # Deleting field 'FactoryState.var_xsa'
        db.delete_column('factoryState_factorystate', 'var_xsa')

        # Deleting field 'FactoryState.var_ysa'
        db.delete_column('factoryState_factorystate', 'var_ysa')

        # Deleting field 'FactoryState.var_zsa'
        db.delete_column('factoryState_factorystate', 'var_zsa')

        # Deleting field 'FactoryState.var_asa'
        db.delete_column('factoryState_factorystate', 'var_asa')

        # Deleting field 'FactoryState.var_1pm'
        db.delete_column('factoryState_factorystate', 'var_1pm')

        # Deleting field 'FactoryState.var_2pm'
        db.delete_column('factoryState_factorystate', 'var_2pm')

        # Deleting field 'FactoryState.var_3pm'
        db.delete_column('factoryState_factorystate', 'var_3pm')

        # Deleting field 'FactoryState.var_4pm'
        db.delete_column('factoryState_factorystate', 'var_4pm')


    models = {
        'factoryState.factorystate': {
            'Meta': {'object_name': 'FactoryState'},
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
            'tabbingOnSpool': ('django.db.models.fields.IntegerField', [], {}),
            'var_1ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_1pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_2ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_2pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_3ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_3pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_4ma': ('django.db.models.fields.IntegerField', [], {}),
            'var_4pm': ('django.db.models.fields.IntegerField', [], {}),
            'var_afr': ('django.db.models.fields.IntegerField', [], {}),
            'var_asa': ('django.db.models.fields.FloatField', [], {}),
            'var_atr': ('django.db.models.fields.FloatField', [], {}),
            'var_avm': ('django.db.models.fields.IntegerField', [], {}),
            'var_xfr': ('django.db.models.fields.IntegerField', [], {}),
            'var_xsa': ('django.db.models.fields.FloatField', [], {}),
            'var_xtr': ('django.db.models.fields.FloatField', [], {}),
            'var_xvm': ('django.db.models.fields.IntegerField', [], {}),
            'var_yfr': ('django.db.models.fields.IntegerField', [], {}),
            'var_ysa': ('django.db.models.fields.FloatField', [], {}),
            'var_ytr': ('django.db.models.fields.FloatField', [], {}),
            'var_yvm': ('django.db.models.fields.IntegerField', [], {}),
            'var_zfr': ('django.db.models.fields.IntegerField', [], {}),
            'var_zsa': ('django.db.models.fields.FloatField', [], {}),
            'var_ztr': ('django.db.models.fields.FloatField', [], {}),
            'var_zvm': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['factoryState']