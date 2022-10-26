from multiprocessing.dummy.connection import Client
from django.contrib import admin
from .models import *

@admin.register(CrudUser)
class CrudUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'age')



