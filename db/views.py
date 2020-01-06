from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse

class Index(View):

	
	def get(self, request):

		if not request.user.is_authenticated:

			return redirect('login/')
			
		else:

			return render(request, 'db/index.html')

class EditRecord(View):

	def get(self, request, id):

		params={}

		params["id"]=id

		return JsonResponse(params)


