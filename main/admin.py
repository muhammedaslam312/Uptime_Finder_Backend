from django.contrib import admin
from . import models

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    model = models.Account
    list_display = ('id','username', 'email','is_staff','is_verified','is_active','last_login','joined_date') 
    
    readonly_fields = ('last_login','joined_date','password')
    ordering = ('joined_date', )
    filter_horizontal =()
    list_filter = ()
    fieldsets =()

# class UrlAdmin(admin.ModelAdmin):
#     model = models.UrlModel
#     list_display = ('id','url', 'interval','added_time') 

# Register your models here.

# class UrlStatusAdmin(admin.ModelAdmin):
#     model = models.UrlModel
#     list_display = ('id','url','added_time','status') 

admin.site.register(models.Account,AccountAdmin)
# admin.site.register(models.UrlModel,UrlAdmin)

# admin.site.register(models.Hello)
# admin.site.register(models.UrlStatus,UrlStatusAdmin)

