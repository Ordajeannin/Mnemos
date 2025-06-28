from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Flashcard

User = get_user_model()

class FlashcardTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

    def test_create_flashcard_model(self):
        flashcard = Flashcard.objects.create(
            title="Test Flashcard",
            content_markdown="# Test",
            next_review_date="2025-07-01T00:00:00Z",
            repetition_count=0,
            easiness_factor=2.5,
            author=self.user
        )
        self.assertEqual(flashcard.title, "Test Flashcard")
        self.assertEqual(flashcard.author, self.user)

    def test_create_flashcard_api(self):
        url = reverse("flashcard-list")
        data = {
            "title": "API Flashcard",
            "content_markdown": "Content from API",
            "next_review_date": "2025-07-01T00:00:00Z",
            "repetition_count": 0,
            "easiness_factor": 2.5
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Flashcard.objects.count(), 1)
        self.assertEqual(Flashcard.objects.get().title, "API Flashcard")

    def test_create_flashcard_unauthenticated(self):
        self.client.logout()
        url = reverse("flashcard-list")
        data = {
            "title": "Unauthenticated Flashcard",
            "content_markdown": "Should fail",
            "next_review_date": "2025-07-01T00:00:00Z",
            "repetition_count": 0,
            "easiness_factor": 2.5
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

