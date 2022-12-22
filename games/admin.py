from django.contrib import admin
from .models import *

class gameAdmin(admin.ModelAdmin):
    list_display = ('game_name','game_id','game_categary','game_version','views','game_sub_categary')
    search_fields = ('game_name','game_id','game_categary','game_version','views','game_sub_categary')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class gamecommentsAdmin(admin.ModelAdmin):
    list_display = ('game','user','sno')
    search_fields = ('game','user','sno','comment')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(game,gameAdmin)
admin.site.register(gamecomments,gamecommentsAdmin)

