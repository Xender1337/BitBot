# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AlgOption.date'
        db.add_column(u'Trade_algoption', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 6, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AlgOption.date'
        db.delete_column(u'Trade_algoption', 'date')


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
            'Meta': {'object_name': 'BitstampUser'},
            'PublicKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'SecretKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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