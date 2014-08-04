# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BtcRate'
        db.create_table(u'Trade_btcrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('volume', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=8)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Trade', ['BtcRate'])


    def backwards(self, orm):
        # Deleting model 'BtcRate'
        db.delete_table(u'Trade_btcrate')


    models = {
        u'Trade.btcrate': {
            'Meta': {'object_name': 'BtcRate'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'})
        }
    }

    complete_apps = ['Trade']