from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	group_no = models.IntegerField('group_no',null=True)
