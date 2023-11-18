
from django.urls import path
from .views import ingest_log, homepage

urlpatterns = [
    path('ingest_log/', ingest_log, name='ingest_log'),
    path('', homepage, name='homepage'),
]
