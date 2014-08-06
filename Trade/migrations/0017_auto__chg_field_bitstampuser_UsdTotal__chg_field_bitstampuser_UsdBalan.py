# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BitstampUser.UsdTotal'
        db.alter_column(u'Trade_bitstampuser', 'UsdTotal', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2))

        # Changing field 'BitstampUser.UsdBalance'
        db.alter_column(u'Trade_bitstampuser', 'UsdBalance', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2))

        # Changing field 'BitstampUser.UsdReserved'
        db.alter_column(u'Trade_bitstampuser', 'UsdReserved', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2))

        # Changing field 'BitstampUser.UsdAvailable'
        db.alter_column(u'Trade_bitstampuser', 'UsdAvailable', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'BitstampUser.UsdTotal'
        db.alter_column(u'Trade_bitstampuser', 'UsdTotal', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=4))

        # Changing field 'BitstampUser.UsdBalance'
        db.alter_column(u'Trade_bitstampuser', 'UsdBalance', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=4))

        # Changing field 'BitstampUser.UsdReserved'
        db.alter_column(u'Trade_bitstampuser', 'UsdReserved', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=4))

        # Changing field 'BitstampUser.UsdAvailable'
        db.alter_column(u'Trade_bitstampuser', 'UsdAvailable', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=4))

    models = {
        u'Trade.algoption': {
            'BuyRate': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'}),
            'Meta': {'object_name': 'AlgOption'},
            'Status': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '2'}),
            'cpt': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Trade.average': {
            'Meta': {'object_name': 'Average'},
            'dayAverage': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthAverage': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'})
        },
        u'Trade.bitstampuser': {
            'AccountName': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'BtcAvailable': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '8'}),
            'BtcBalance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '8'}),
            'BtcReserved': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '8'}),
            'BtcTotal': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '8'}),
            'Fee': ('django.db.models.fields.DecimalField', [], {'default': '0.05', 'max_digits': '3', 'decimal_places': '2'}),
            'Meta': {'object_name': 'BitstampUser'},
            'PublicKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'SecretKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'UsdAvailable': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'UsdBalance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'UsdReserved': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'UsdTotal': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '2'}),
            'UserID': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Trade.btcvalue': {
            'Meta': {'object_name': 'BtcValue'},
            'ask': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'high': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'})
        },
        u'Trade.eurusd': {
            'Meta': {'object_name': 'EurUsd'},
            'buy': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '4'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sell': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '4'})
        }
    }

    complete_apps = ['Trade']