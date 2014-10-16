from quote_app.models import QuoteItemType, Vendor, QuoteItem, VendorQuote
from rest_framework import serializers


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name')