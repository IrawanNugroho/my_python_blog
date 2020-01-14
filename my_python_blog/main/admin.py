from django.contrib import admin
from django.utils.html import format_html
from . import models


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display    =   ('name', 'description', 'updated_by', 'updated_at')
    exclude         =   ('created_by', 'updated_by')
admin.site.register(models.Status, StatusAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display        =   ('name', 'updated_by', 'updated_at')
    exclude             =   ('created_by', 'updated_by')
    prepopulated_fields =   {"slug":("name",)}
admin.site.register(models.Tag, TagAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display    =   ('title', 'author', 'updated_by', 'updated_at')
    exclude         =   ('created_by', 'updated_by')
    readonly_fields =   ('thumbnail',)
admin.site.register(models.Image, ImageAdmin)