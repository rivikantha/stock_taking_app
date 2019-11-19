from django.shortcuts import render
from django.views.generic import View
from pprint import pprint

class StockTake(View):
	
	def get(self,request):

		print('hello')
		print(request.user)

		return render(request, 'user/stock_take.html')




