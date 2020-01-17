from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse,HttpResponseRedirect
from .models import Database
from .forms import DatabaseForm

class Index(View):

	
	def get(self, request):

		if not request.user.is_authenticated:

			return redirect('login/')
			
		else:

			return render(request, 'db/index.html')

class EditRecord(View):

	def get(self, request, barcode):

		params = {}

		params["id"] = id

		db_record = Database.objects.get(barcode=barcode)

		db_record_form = DatabaseForm(instance=db_record)

		params['db_form'] = db_record_form

		return render(request, 'db/update_record.html',params)

	def post(self, request):

		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

		form = DatabaseForm(request.POST)

		if form.is_valid():

			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
			
			

			barcode = form.cleaned_data('barcode')

			db_record = Database.objects.get(barcode=barcode)
			db_record.title=form.cleaned_data['title']
			db_record.author=form.cleaned_data['author']
			db_record.classification=form.cleaned_data['classification']
			db_record.price=form.cleaned_data['price']
			db_record.pub_year=form.cleaned_data['pub_year']
			db_record.edited=True

			db_record.save()

			return HttpResponseRedirect('/stock_take/'+ form.cleaned_data['barcode'])

		return HttpResponseRedirect('/stock_take/'+ form.cleaned_data['barcode'])

