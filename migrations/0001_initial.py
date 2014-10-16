# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuoteItemType'
        db.create_table('quote_app_quoteitemtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('quote_app', ['QuoteItemType'])

        # Adding model 'Vendor'
        db.create_table('quote_app_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('quote_app', ['Vendor'])

        # Adding model 'QuoteItem'
        db.create_table('quote_app_quoteitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quote_app.QuoteItemType'])),
            ('vendorQuote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quote_app.VendorQuote'])),
        ))
        db.send_create_signal('quote_app', ['QuoteItem'])

        # Adding model 'VendorQuote'
        db.create_table('quote_app_vendorquote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('quote_app', ['VendorQuote'])


    def backwards(self, orm):
        # Deleting model 'QuoteItemType'
        db.delete_table('quote_app_quoteitemtype')

        # Deleting model 'Vendor'
        db.delete_table('quote_app_vendor')

        # Deleting model 'QuoteItem'
        db.delete_table('quote_app_quoteitem')

        # Deleting model 'VendorQuote'
        db.delete_table('quote_app_vendorquote')


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
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['quote_app']