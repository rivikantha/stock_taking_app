"""stock_taking_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from db.views import Index,EditRecord
from user.views import StockTake,EditStockEntry,DeleteStockEntry,Statistics,StatDaily

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Index.as_view()),
    path('',include('django.contrib.auth.urls')),    
    re_path(r'^stock_take/(\w*)/*$',login_required(StockTake.as_view())),
    re_path(r'^edit_stock_entry/(\w*)/*$',login_required(EditStockEntry.as_view())),
    re_path(r'^delete_stock_entry/(\w*)/*$',login_required(DeleteStockEntry.as_view())),
    path('statistics/',login_required(Statistics.as_view())),
    path('stat_daily/',login_required(StatDaily.as_view())),
    re_path(r'^edit_db_record_form/(\w*)/*$',login_required(EditRecord.as_view())),
    path('edit_db_record/',login_required(EditRecord.as_view())),     
]
