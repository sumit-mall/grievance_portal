from portal.models import Complaint, Contact
from django.contrib import admin

# Register your models here.


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    '''Admin View for News'''

    list_display = ('name','enrollment','department','date','status')
    list_filter = ('status','date')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for News'''

    list_display = ('name','reason','date')
    list_filter = ('reason','date')