from django.db import models

# Create your models here.
class QuoteItemType(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	
class Vendor(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class QuoteItem(models.Model):
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	type = models.ForeignKey('QuoteItemType')
	vendorQuote = models.ForeignKey('VendorQuote')
	def __str__(self):
		return self.description
	
class VendorQuote(models.Model):
	date = models.DateField()
	number = models.CharField(max_length=100)
	file = models.FileField(upload_to='quote_files', blank=True)
	vendor = models.ForeignKey('Vendor')
	def __str__(self):
		return self.vendor.name+' '+self.number