
from django.urls import path
from .views import ingest_log, homepage, LogSearchView

urlpatterns = [
    path('ingest_log/', ingest_log, name='ingest_log'),
    path('log_search/', LogSearchView.as_view(), name='log_search'),
    path('', homepage, name='homepage'),
]
