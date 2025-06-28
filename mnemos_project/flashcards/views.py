from rest_framework import viewsets, permissions
from .models import Flashcard
from .serializers import FlashcardSerializer

print("✅ FLASHCARD VIEWSET LOADED")

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print("DEBUG request.user:", self.request.user)
        serializer.save(author=self.request.user)


