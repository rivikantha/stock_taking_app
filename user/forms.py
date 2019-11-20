from django import forms

class StockTakingForm(forms.Form):

	STATUS = [
	
		('N', 'Normal'),
		('D', 'Duplicate'),
		('O', 'Other'),
		('M', 'Missmatch')
	    
	]

	barcode = forms.CharField(label="Barcode", max_length=10)
	status = forms.ChoiceField(choices=STATUS, required=False)
	remarks = forms.CharField(label="remarks", widget=forms.Textarea(attrs={'rows': 1,'cols': 85}), max_length=750, required=False)

