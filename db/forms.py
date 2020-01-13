from django.forms import ModelForm
from .models import Database


class DatabaseForm(ModelForm):

	class Meta:

		model=Database
		fields=['barcode','acc_no','title','author','loc','classification','price','pub_year','edited']