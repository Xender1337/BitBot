# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BitstampUser.UserAccount'
        db.delete_column(u'Trade_bitstampuser', 'UserAccount')

        # Deleting field 'BitstampUser.ApiKey'
        db.delete_column(u'Trade_bitstampuser', 'ApiKey')

        # Adding field 'BitstampUser.AccountName'
        db.add_column(u'Trade_bitstampuser', 'AccountName',
                      self.gf('django.db.models.fields.CharField')(default='test', unique=True, max_length=100),
                      keep_default=False)

        # Adding field 'BitstampUser.UserID'
        db.add_column(u'Trade_bitstampuser', 'UserID',
                      self.gf('django.db.models.fields.IntegerField')(default='1234658', unique=True, max_length=10),
                      keep_default=False)

        # Adding field 'BitstampUser.PublicKey'
        db.add_column(u'Trade_bitstampuser', 'PublicKey',
                      self.gf('django.db.models.fields.CharField')(default='1234465', unique=True, max_length=255),
                      keep_default=False)

        # Adding field 'BitstampUser.SecretKey'
        db.add_column(u'Trade_bitstampuser', 'SecretKey',
                      self.gf('django.db.models.fields.CharField')(default='13245', unique=True, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BitstampUser.UserAccount'
        db.add_column(u'Trade_bitstampuser', 'UserAccount',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=100, unique=True),
                      keep_default=False)

        # Adding field 'BitstampUser.ApiKey'
        db.add_column(u'Trade_bitstampuser', 'ApiKey',
                      self.gf('django.db.models.fields.CharField')(default='fzefez', max_length=255, unique=True),
                      keep_default=False)

        # Deleting field 'BitstampUser.AccountName'
        db.delete_column(u'Trade_bitstampuser', 'AccountName')

        # Deleting field 'BitstampUser.UserID'
        db.delete_column(u'Trade_bitstampuser', 'UserID')

        # Deleting field 'BitstampUser.PublicKey'
        db.delete_column(u'Trade_bitstampuser', 'PublicKey')

        # Deleting field 'BitstampUser.SecretKey'
        db.delete_column(u'Trade_bitstampuser', 'SecretKey')


    models = {
        u'Trade.algoption': {
            'BuyRate': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'}),
            'Meta': {'object_name': 'AlgOption'},
            'Status': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '2'}),
            'cpt': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '2'}),
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