from django import forms

class StockTakingForm(forms.Form):

	STATUS = [
	
		('D', 'Duplicate'),
		('O', 'Other'),
		('M', 'Missmatch'),
	    
	]

	barcode = forms.CharField(label="Barcode", max_length=10)
	staus = forms.ChoiceField(choices=STATUS, required=False)
	remarks = forms.CharField(label="remarks", widget=forms.Textarea(attrs={'rows': 1,'cols': 85}), max_length=750, required=False)

