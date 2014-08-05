# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BtcRate.high'
        db.add_column(u'Trade_btcrate', 'high',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=8, decimal_places=2),
                      keep_default=False)

        # Adding field 'BtcRate.low'
        db.add_column(u'Trade_btcrate', 'low',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=8, decimal_places=2),
                      keep_default=False)

        # Adding field 'BtcRate.ask'
        db.add_column(u'Trade_btcrate', 'ask',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=8, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BtcRate.high'
        db.delete_column(u'Trade_btcrate', 'high')

        # Deleting field 'BtcRate.low'
        db.delete_column(u'Trade_btcrate', 'low')

        # Deleting field 'BtcRate.ask'
        db.delete_column(u'Trade_btcrate', 'ask')


    models = {
        u'Trade.btcrate': {
            'Meta': {'object_name': 'BtcRate'},
            'ask': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'high': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'})
        }
    }

    complete_apps = ['Trade']