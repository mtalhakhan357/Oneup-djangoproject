from django.contrib import admin
from .models import *
# Register your models here.


class appAdmin(admin.ModelAdmin):
    list_display = ('app_name','app_id','app_categary','app_version','views','app_sub_categary')
    search_fields = ('app_id','app_name','app_categary','app_version','views','app_sub_categary')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
class appcommentsAdmin(admin.ModelAdmin):
    list_display = ('app','user','sno')
    search_fields = ('app','user','sno','comment')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(app,appAdmin)
admin.site.register(appcomments,appcommentsAdmin)