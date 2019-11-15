from django import forms

class StockTakingForms(forms.Form):

	STATUS = [
	
		('D', 'Duplicate'),
		('O', 'Other'),
		('M', 'Missmatch'),
	    
	]

	barcode = forms.CharField(label="Barcode", max_length=10)
	staus = forms.ChoiceField(choices=STATUS)
	remarks = forms.CharField(label="Barcode", widget=forms.Textarea(attrs={'rows': 1,'cols': 85}), max_length=750)

