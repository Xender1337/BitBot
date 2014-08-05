# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BtcRate'
        db.delete_table(u'Trade_btcrate')

        # Adding model 'BtcValue'
        db.create_table(u'Trade_btcvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('high', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('low', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('ask', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('volume', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=8)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Trade', ['BtcValue'])

        # Adding model 'AlgOption'
        db.create_table(u'Trade_algoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Status', self.gf('django.db.models.fields.IntegerField')(unique=True, max_length=2)),
            ('BuyRate', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=8)),
        ))
        db.send_create_signal(u'Trade', ['AlgOption'])


    def backwards(self, orm):
        # Adding model 'BtcRate'
        db.create_table(u'Trade_btcrate', (
            ('high', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('low', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('ask', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('volume', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=8)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'Trade', ['BtcRate'])

        # Deleting model 'BtcValue'
        db.delete_table(u'Trade_btcvalue')

        # Deleting model 'AlgOption'
        db.delete_table(u'Trade_algoption')


    models = {
        u'Trade.algoption': {
            'BuyRate': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'}),
            'Meta': {'object_name': 'AlgOption'},
            'Status': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Trade.average': {
            'Meta': {'object_name': 'Average'},
            'dayAverage': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthAverage': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'})
        },
        u'Trade.bitstampuser': {
            'ApiKey': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'Meta': {'object_name': 'BitstampUser'},
            'UserAccount': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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