from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class Index(View):

	
	def get(self, request):

		if not request.user.is_authenticated:

			return redirect('login/')
			
		else:

			return render(request, 'db/index.html')



