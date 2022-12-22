from django.contrib import admin
from .models import *

class contactrequestsAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_id','user_email','user_subject','user_type')
    search_fields = ('user_id','user_name','user_email','user_subject','user_type')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class despAndTextAdmin(admin.ModelAdmin):
    list_display = ('text_name','text_id','text_tittle','text_body')
    search_fields = ('text_id','text_name','text_tittle','text_body')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class statusticsAdmin(admin.ModelAdmin):
    list_display = ('page_name','page_views','page_id')
    search_fields = ('page_id','page_name','page_href','page_type','page_views')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class page_detailsAdmin(admin.ModelAdmin):
    list_display = ('page_name','page_id')
    search_fields = ('page_id','page_name','page_tittle')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(contactrequests,contactrequestsAdmin)
admin.site.register(despAndText,despAndTextAdmin)
admin.site.register(statustics,statusticsAdmin)
admin.site.register(page_details,page_detailsAdmin)
admin.site.register(Profile)
# admin.site.register(
# admin.site.register(
# admin.site.register(