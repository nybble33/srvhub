from django.contrib import admin

# Register your models here.

from cms.models import Web_Page

class Web_PageAdmin(admin.ModelAdmin):
    list_display = ('modified', 'url', 'token', 'status')
    ordering = ['-modified']


admin.site.register(Web_Page, Web_PageAdmin)