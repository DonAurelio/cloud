from django.contrib import admin

from event.models import *

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
    	'id','name','venue','address','start_date',
    	'end_date','category','classification'
    )
    search_fields = ('id','name',)
