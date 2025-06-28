from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Flashcard

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'next_review_date', 'public')
    search_fields = ('title', 'content_markdown')
    list_filter = ('public', 'tags')
