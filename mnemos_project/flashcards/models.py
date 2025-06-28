from django.db import models

# Create your models here.
import uuid
from django.conf import settings
from django.db import models

class Flashcard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content_markdown = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    next_review_date = models.DateTimeField()
    repetition_count = models.PositiveIntegerField(default=0)
    easiness_factor = models.FloatField(default=2.5)
    last_quality = models.PositiveSmallIntegerField(null=True, blank=True)
    tags = models.JSONField(default=list, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='flashcards'
    )
    public = models.BooleanField(default=False)
    last_ai_score = models.PositiveSmallIntegerField(null=True, blank=True)
    last_ai_feedback = models.TextField(blank=True)

    def __str__(self):
        return self.title
