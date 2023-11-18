
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LogEntry
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