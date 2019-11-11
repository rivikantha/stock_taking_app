from django.contrib import admin
from .models import Database

class DatabaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Database, DatabaseAdmin)

