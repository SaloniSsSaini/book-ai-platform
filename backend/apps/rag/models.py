# backend/apps/rag/models.py

from django.db import models

class ChatHistory(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:50]


class QueryLog(models.Model):
    query = models.TextField(unique=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.query} ({self.count})"