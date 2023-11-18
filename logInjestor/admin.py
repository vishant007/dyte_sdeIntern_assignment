# log_ingestor/admin.py
from django.contrib import admin
from .models import LogEntry
import json

class LogEntryAdmin(admin.ModelAdmin):
    # your existing configurations...

    def save_model(self, request, obj, form, change):
        # Save the LogEntry instance
        super().save_model(request, obj, form, change)

        # Get the data as a dictionary
        log_data = {
            'level': obj.level,
            'message': obj.message,
            'resourceId': obj.resourceId,
            'timestamp': obj.timestamp.isoformat(),  # Convert to string
            'traceId': obj.traceId,
            'spanId': obj.spanId,
            'commit': obj.commit,
            'metadata':{
            'parentResourceId': obj.parentResourceId,
            }
        }

        # Save the data to a JSON file
        json_file_path = 'dyte_sdeIntern_assignment/json_data/log_entries.json'
        with open(json_file_path, 'a') as json_file:
            json.dump(log_data, json_file)
            json_file.write('\n')  

# Register the LogEntry model with the custom admin class
admin.site.register(LogEntry, LogEntryAdmin)
