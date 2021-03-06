from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

	group_no = models.IntegerField('group_no',null=True)


class StockEntry(models.Model):

	STATUS = [
	
		('D', 'Duplicate'),
		('O', 'Other'),
		('M', 'Missmatch'),
	    
	]

	id = models.AutoField(primary_key=True)
	barcode = models.CharField('barcode',max_length=10)
	status = models.CharField('status',max_length=1, choices=STATUS,null=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, default="")
	shelf_no = models.CharField('shelf no',max_length=20)
	remarks = models.TextField('Remarks',null=True)
	date = models.DateField(auto_now=True)


