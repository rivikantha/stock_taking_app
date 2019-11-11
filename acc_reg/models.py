from django.db import models

class AccReg(models.Model):

	id = models.IntegerField('id',unique=True, db_index=True, primary_key = True)
	barcode = models.CharField('barcode',max_length=10,null=True,blank=True)
	inv_folio_no = models.CharField('inventory folio number',max_length=10,null=True,blank=True)

	def __str__(self):

		return self.barcode
	
