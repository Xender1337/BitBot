# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BitstampUser.BtcTotal'
        db.add_column(u'Trade_bitstampuser', 'BtcTotal',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=8),
                      keep_default=False)

        # Adding field 'BitstampUser.UsdTotal'
        db.add_column(u'Trade_bitstampuser', 'UsdTotal',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=4),
                      keep_default=False)


        # Changing field 'BitstampUser.BtcBalance'
        db.alter_column(u'Trade_bitstampuser', 'BtcBalance', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=8))

        # Changing field 'BitstampUser.BtcReserved'
        db.alter_column(u'Trade_bitstampuser', 'BtcReserved', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=8))

        # Changing field 'BitstampUser.BtcAvailable'
        db.alter_column(u'Trade_bitstampuser', 'BtcAvailable', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=8))

    def backwards(self, orm):
        # Deleting field 'BitstampUser.BtcTotal'
        db.delete_column(u'Trade_bitstampuser', 'BtcTotal')

        # Deleting field 'BitstampUser.UsdTotal'
        db.delete_column(u'Trade_bitstampuser', 'UsdTotal')


        # Changing field 'BitstampUser.BtcBalance'
        db.alter_column(u'Trade_bitstampuser', 'BtcBalance', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=8))

        # Changing field 'BitstampUser.BtcReserved'
        db.alter_column(u'Trade_bitstampuser', 'BtcReserved', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=8))

        # Changing field 'BitstampUser.BtcAvailable'
        db.alter_column(u'Trade_bitstampuser', 'BtcAvailable', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=8))

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
            'BtcAvailable': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '8'}),
            'BtcBalance': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '8'}),
            'BtcReserved': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '8'}),
            'BtcTotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '8'}),
            'Fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'Meta': {'object_name': 'BitstampUser'},
            'PublicKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'SecretKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'UsdAvailable': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
            'UsdBalance': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
            'UsdReserved': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
            'UsdTotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
            'UserID': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Trade.btcvalue': {
            'Meta': {'object_name': 'BtcValue'},
            'ask': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
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