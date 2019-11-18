from django.shortcuts import render
from django.views.generic import View
from .forms import StockTakingForm
from .models import StockEntry
from django.http import HttpResponseRedirect

class StockTake(View):
	
	def get(self,request):

		params = {}

		form = StockTakingForm()

		params['form'] = form

		return render(request, 'user/stock_take.html', params)

	def post(self,request):

		form = StockTakingForm(request.POST)

		if form.is_valid():

			stock_entry = StockEntry(

					user = request.user,

					barcode = form.cleaned_data['barcode'],

					status = form.cleaned_data['status'],

					remarks = form.cleaned_data['remarks']

				)

			stock_entry.save()

			return HttpResponseRedirect('stock_entry/')

			




