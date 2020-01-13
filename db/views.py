from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Database
from .forms import DatabaseForm

class Index(View):

	
	def get(self, request):

		if not request.user.is_authenticated:

			return redirect('login/')
			
		else:

			return render(request, 'db/index.html')

class EditRecord(View):

	def get(self, request, id):

		params = {}

		params["id"] = id

		db_record = Database.objects.get(id=id)

		db_record_form = DatabaseForm(instance=db_record)

		params['db_form'] = db_record_form

		return render(request, 'db/update_record.html',params)


