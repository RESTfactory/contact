"""API Control Django admin."""
from django.contrib import admin
from .models import App, OrganizationalUnitType, OrganizationalUnit


class AppAdmin(admin.ModelAdmin):
    readonly_fields = ('api_key',)


admin.site.register(OrganizationalUnitType)
admin.site.register(OrganizationalUnit)
admin.site.register(App, AppAdmin)
