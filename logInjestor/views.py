
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.views import FilterView
from .models import LogEntry
from .filters import LogEntryFilter
from django.shortcuts import render
import json

@csrf_exempt
def ingest_log(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        timestamp = data.get('timestamp')
        log_message = data.get('log_message')

        # Save to the database
        LogEntry.objects.create(timestamp=timestamp, log_message=log_message)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def homepage(request):
    # Retrieve log entries from the database (you can add ordering or filtering as needed)
    log_entries = LogEntry.objects.all()

    return render(request, 'homepage.html', {'log_entries': log_entries})

class LogSearchView(FilterView):
    model = LogEntry
    template_name = 'log_search.html'
    filterset_class = LogEntryFilter
    context_object_name = 'log_entries'