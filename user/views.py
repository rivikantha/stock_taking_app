from django.shortcuts import render
from django.views.generic import View
from pprint import pprint
from .forms import StockTakingForm
from .models import StockEntry
from django.http import HttpResponseRedirect

class StockTake(View):
	
	def get(self,request,barcode=''):

		params = {}

		entries_so_far = StockEntry.objects.filter(user=request.user).order_by('-id')[:5]	

		params['entries'] = reversed(entries_so_far)	

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

			return HttpResponseRedirect('/stock_take/'+ form.cleaned_data['barcode'])

			





