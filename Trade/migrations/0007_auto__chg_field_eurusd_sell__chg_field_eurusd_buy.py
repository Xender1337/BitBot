# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EurUsd.sell'
        db.alter_column(u'Trade_eurusd', 'sell', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=4))

        # Changing field 'EurUsd.buy'
        db.alter_column(u'Trade_eurusd', 'buy', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=4))

    def backwards(self, orm):

        # Changing field 'EurUsd.sell'
        db.alter_column(u'Trade_eurusd', 'sell', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

        # Changing field 'EurUsd.buy'
        db.alter_column(u'Trade_eurusd', 'buy', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

    models = {
        u'Trade.bitstampuser': {
            'ApiKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'Meta': {'object_name': 'BitstampUser'},
            'UserAccount': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Trade.btcrate': {
            'Meta': {'object_name': 'BtcRate'},
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