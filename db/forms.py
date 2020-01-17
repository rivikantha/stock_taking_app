from django.forms import ModelForm
from .models import Database
from django import forms


class DatabaseForm(ModelForm):

	class Meta:

		model=Database
		fields=['title','author','loc','classification','price','pub_year','edited']
		widgets = {'barcode': forms.HiddenInput()}