from django.contrib import admin
from .models import Brainwork
# Register your models here.
class BrainworkAdmin(admin.ModelAdmin):
    list_display = ['Title','Descriptions']

admin.site.register(Brainwork,BrainworkAdmin)

admin.site.site_header='ROHIT'