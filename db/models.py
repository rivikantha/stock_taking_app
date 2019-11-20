from django.db import models

class Database(models.Model):


	id = models.IntegerField('id',unique=True, db_index=True, primary_key = True)
	barcode = models.CharField('barcode',max_length=10,null=True,blank=True)
	acc_no = models.CharField('accession number',max_length=10,null=True,blank=True)
	title = models.CharField('title',max_length=200,null=True,blank=True)
	author = models.CharField('author',max_length=100,null=True,blank=True)
	loc = models.CharField('location code',max_length=10,null=True,blank=True)	
	classification = models.CharField('classification',max_length=10,null=True,blank=True)	
	price = models.FloatField('price',blank=True)	
	pub_year = models.CharField('publication year',max_length=10,null=True,blank=True)
	

	def __str__(self):

		return self.barcode

	

