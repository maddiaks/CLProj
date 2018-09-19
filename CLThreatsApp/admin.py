from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import Threat

# Register your models here.

class ThreatResource(resources.ModelResource):
    class Meta:
        model = Threat
        fields = ('ip_address', 'domainname', 'reverse_lookup', 'description',)


class ThreatAdmin(ImportExportModelAdmin):
    resource_class = ThreatResource

    list_display = ['ip_address', 'domainname', 'reverse_lookup', 'description', 'created_at', 'updated_at']
    list_filter = ['ip_address', 'domainname', 'created_at', 'updated_at']
    search_fields = ['ip_address', 'domainname']
    list_display_links = list_display

    class Meta:
        model = Threat

admin.site.register(Threat, ThreatAdmin)