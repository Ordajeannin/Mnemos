from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
