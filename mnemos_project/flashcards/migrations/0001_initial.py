# Generated by Django 5.2.3 on 2025-06-27 16:42

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content_markdown', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('next_review_date', models.DateTimeField()),
                ('repetition_count', models.PositiveIntegerField(default=0)),
                ('easiness_factor', models.FloatField(default=2.5)),
                ('last_quality', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('tags', models.JSONField(blank=True, default=list)),
                ('public', models.BooleanField(default=False)),
                ('last_ai_score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('last_ai_feedback', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
