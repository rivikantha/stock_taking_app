from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class StockTake(View):

	@login_required
	def get(self,request):

		return render(request, 'user/stock_take.html')




