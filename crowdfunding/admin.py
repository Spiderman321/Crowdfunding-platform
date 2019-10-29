from django.contrib import admin

# Register your models here.
from .models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('idNum','name','phoneNum')
admin.site.register(Sponsor,SponsorAdmin)
