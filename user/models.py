from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

<<<<<<< HEAD
=======
	"""
	
	Custom User Model

	"""

>>>>>>> 943a41477ba2d96432f8ac9dd9769b6da570d4a9
	group_no = models.IntegerField('group_no',null=True)
