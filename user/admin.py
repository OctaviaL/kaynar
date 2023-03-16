from django.contrib import admin
from user.models import *
from allauth.socialaccount.models import SocialApp

admin.site.unregister(SocialApp)

@admin.register(SocialApp)
class SocialAppAdmin(admin.ModelAdmin):
    list_display = ('provider', 'name', 'client_id')
    list_filter = ('provider',)
    search_fields = ('name', 'client_id')

admin.site.register(CustomUser)
