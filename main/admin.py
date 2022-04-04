from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from main.models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('datetime_field', 'ip_field', 'status')
    list_filter = (('datetime_field', DateRangeFilter), 'ip_field', 'status')
    search_fields = ('ip_field', )
    search_help_text = 'поиск по ip_field'
  

