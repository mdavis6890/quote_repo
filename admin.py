from django.contrib import admin
from quote_app.models import Vendor, QuoteItemType, QuoteItem, VendorQuote

admin.site.register(Vendor)
admin.site.register(QuoteItemType)
admin.site.register(QuoteItem)
admin.site.register(VendorQuote)