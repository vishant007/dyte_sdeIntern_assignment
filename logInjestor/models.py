from django.db import models

class LogEntry(models.Model):
    level = models.CharField(max_length=10)
    message = models.TextField()
    resourceId = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    traceId = models.CharField(max_length=20)
    spanId = models.CharField(max_length=20)
    commit = models.CharField(max_length=20)
    parentResourceId = models.CharField(max_length=40)


    def __str__(self):
        return f"{self.timestamp} - {self.message}"