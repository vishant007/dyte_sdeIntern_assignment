import django_filters
from .models import LogEntry

class LogEntryFilter(django_filters.FilterSet):
    class Meta:
        model = LogEntry
        fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'parentResourceId']
