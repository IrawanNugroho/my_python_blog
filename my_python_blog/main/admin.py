from django.contrib import admin
from django.utils.html import format_html
from . import models


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display    =   ('name', 'description', 'created_by', 'updated_by')
admin.site.register(models.Status, StatusAdmin)