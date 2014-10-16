# Create your views here.
from quote_app.models import QuoteItemType, Vendor, QuoteItem, VendorQuote
from rest_framework import viewsets
from quote_app.serializers import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer