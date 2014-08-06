# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.BitstampUser'
        db.add_column(u'Trade_order', 'BitstampUser',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['Trade.BitstampUser']),
                      keep_default=False)

        # Removing M2M table for field Order on 'BitstampUser'
        db.delete_table(db.shorten_name(u'Trade_bitstampuser_Order'))


    def backwards(self, orm):
        # Deleting field 'Order.BitstampUser'
        db.delete_column(u'Trade_order', 'BitstampUser_id')

        # Adding M2M table for field Order on 'BitstampUser'
        m2m_table_name = db.shorten_name(u'Trade_bitstampuser_Order')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bitstampuser', models.ForeignKey(orm[u'Trade.bitstampuser'], null=False)),
            ('order', models.ForeignKey(orm[u'Trade.order'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bitstampuser_id', 'order_id'])


    models = {
        u'Trade.algoption': {
            'BuyRate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '8'}),
            'Meta': {'object_name': 'AlgOption'},
            'Status': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'cpt': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
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
        },
        u'Trade.order': {
            'Amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '8'}),
            'BitstampUser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Trade.BitstampUser']"}),
            'Meta': {'object_name': 'Order'},
            'OrderId': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '20'}),
            'OrderType': ('django.db.models.fields.IntegerField', [], {}),
            'Price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '8'}),
            'RequestType': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Trade']