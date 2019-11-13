from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,StockEntry

class StockEntryAdmin(admin.ModelAdmin):
	pass

admin.site.register(StockEntry, StockEntryAdmin)

admin.site.register(User,UserAdmin)


