from django.shortcuts import render
from django.views.generic import View
from pprint import pprint
from .forms import StockTakingForm
from .models import StockEntry
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from db.models import Database
from django.db.models import Count

class StockTake(View):
	
	def get(self,request,barcode):

		params = {}	

		if(barcode != ''):					

			db_record = Database.objects.get(barcode=barcode)			
			
			if(db_record):

				params['db_record']=db_record


		entries_so_far = StockEntry.objects.filter(user=request.user).order_by('-id')[:5]	

		params['entries'] = reversed(entries_so_far)

		if 'shelf_no' not in request.session:

			shelf_no = ""

		else:

			shelf_no = request.session['shelf_no']	

		form = StockTakingForm(initial={'status': 'N','shelf_no':shelf_no})

		params['form'] = form

		return render(request, 'user/stock_take.html', params)

	def post(self,request,barcode):

		form = StockTakingForm(request.POST)

		if form.is_valid():

			if(form.cleaned_data['is_update']):

				id = form.cleaned_data['id']

				stock_entry = StockEntry.objects.get(id=id)

				stock_entry.barcode=form.cleaned_data['barcode']
				stock_entry.status=form.cleaned_data['status']
				stock_entry.shelf_no=form.cleaned_data['shelf_no']
				stock_entry.remarks=form.cleaned_data['remarks']

				stock_entry.save()

				request.session['shelf_no']	= form.cleaned_data['shelf_no']

				return HttpResponseRedirect('/stock_take/'+ form.cleaned_data['barcode'])


			stock_entry = StockEntry(

					user = request.user,

					barcode = form.cleaned_data['barcode'],

					status = form.cleaned_data['status'],

					shelf_no = form.cleaned_data['shelf_no'],

					remarks = form.cleaned_data['remarks']

				)

			stock_entry.save()

			request.session['shelf_no']	= form.cleaned_data['shelf_no']

			return HttpResponseRedirect('/stock_take/'+ form.cleaned_data['barcode'])

class EditStockEntry(View):

	def get(self,request,id):
		

		params={}

		entries_so_far = StockEntry.objects.filter(user=request.user).order_by('-id')[:5]	

		params['entries'] = reversed(entries_so_far)

		stock_entry = StockEntry.objects.get(id=id)

		data = {'id':id,
				'barcode':stock_entry.barcode,
				'status':stock_entry.status,
				'remarks':stock_entry.remarks,
				'shelf_no':stock_entry.shelf_no,
				'is_update':True
				}

		form = StockTakingForm(data)		

		params['form'] = form

		return render(request, 'user/stock_take.html', params)

class DeleteStockEntry(View):

	def get(self,request,id):

		stock_entry = StockEntry.objects.get(id=id)

		stock_entry.delete()

		return HttpResponseRedirect('/stock_take/')


class Statistics(View):

	def get(self,request):		

		return render(request,'user/statistics.html')		


class StatDaily(View):

	def get(self,request):

		results = StockEntry.objects.all().values('date').annotate(total=Count('date')).order_by('date')

		labels = []
		data= []

		for result in results:

			formatedDate = result['date'].strftime("%Y-%m-%d")
			total = result['total']	

			labels.append(formatedDate)
			data.append(total)

		param={

			"labels":labels,
			"chart_data":data,
		}
			
		return JsonResponse(param,safe=False)









			





