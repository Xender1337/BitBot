# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BitstampUser.BtcBalance'
        db.add_column(u'Trade_bitstampuser', 'BtcBalance',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=8),
                      keep_default=False)

        # Adding field 'BitstampUser.UsdBalance'
        db.add_column(u'Trade_bitstampuser', 'UsdBalance',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=4),
                      keep_default=False)

        # Adding field 'BitstampUser.BtcAvailable'
        db.add_column(u'Trade_bitstampuser', 'BtcAvailable',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=8),
                      keep_default=False)

        # Adding field 'BitstampUser.UsdAvailable'
        db.add_column(u'Trade_bitstampuser', 'UsdAvailable',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=4),
                      keep_default=False)

        # Adding field 'BitstampUser.BtcReserved'
        db.add_column(u'Trade_bitstampuser', 'BtcReserved',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=8),
                      keep_default=False)

        # Adding field 'BitstampUser.UsdReserved'
        db.add_column(u'Trade_bitstampuser', 'UsdReserved',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=16, decimal_places=4),
                      keep_default=False)

        # Adding field 'BitstampUser.Fee'
        db.add_column(u'Trade_bitstampuser', 'Fee',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BitstampUser.BtcBalance'
        db.delete_column(u'Trade_bitstampuser', 'BtcBalance')

        # Deleting field 'BitstampUser.UsdBalance'
        db.delete_column(u'Trade_bitstampuser', 'UsdBalance')

        # Deleting field 'BitstampUser.BtcAvailable'
        db.delete_column(u'Trade_bitstampuser', 'BtcAvailable')

        # Deleting field 'BitstampUser.UsdAvailable'
        db.delete_column(u'Trade_bitstampuser', 'UsdAvailable')

        # Deleting field 'BitstampUser.BtcReserved'
        db.delete_column(u'Trade_bitstampuser', 'BtcReserved')

        # Deleting field 'BitstampUser.UsdReserved'
        db.delete_column(u'Trade_bitstampuser', 'UsdReserved')

        # Deleting field 'BitstampUser.Fee'
        db.delete_column(u'Trade_bitstampuser', 'Fee')


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
            'BtcAvailable': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '8'}),
            'BtcBalance': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '8'}),
            'BtcReserved': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '8'}),
            'Fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'Meta': {'object_name': 'BitstampUser'},
            'PublicKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'SecretKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'UsdAvailable': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
            'UsdBalance': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
            'UsdReserved': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'}),
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