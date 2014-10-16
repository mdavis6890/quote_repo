# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'VendorQuote.vendor'
        db.add_column('quote_app_vendorquote', 'vendor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['quote_app.Vendor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'VendorQuote.vendor'
        db.delete_column('quote_app_vendorquote', 'vendor_id')


    models = {
        'quote_app.quoteitem': {
            'Meta': {'object_name': 'QuoteItem'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quote_app.QuoteItemType']"}),
            'vendorQuote': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quote_app.VendorQuote']"})
        },
        'quote_app.quoteitemtype': {
            'Meta': {'object_name': 'QuoteItemType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quote_app.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quote_app.vendorquote': {
            'Meta': {'object_name': 'VendorQuote'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quote_app.Vendor']"})
        }
    }

    complete_apps = ['quote_app']