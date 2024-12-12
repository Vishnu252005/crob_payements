from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from events.models import EventRegistration
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class EventRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.event_name = 'Roborace'

    def test_event_registration_with_screenshot(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('submit-event', args=[self.event_name])
        # Create a simple in-memory file
        screenshot = SimpleUploadedFile(
            name='test_screenshot.png',
            content=b'\x47\x49\x46\x38\x39\x61',  # Minimal GIF header bytes
            content_type='image/png'
        )
        response = self.client.post(url, {
            'leader_name': 'Leader',
            'team_name': 'TeamX',
            'leader_email': 'leader@example.com',
            'leader_phone': '1234567890',
            'college': 'College',
            'year': '2024',
            'branch': 'Engineering',
            'team_members[]': ['Member1', 'Member2'],
            'screenshot': screenshot,  # Provide screenshot
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(EventRegistration.objects.filter(team_name='TeamX').exists())

    def test_event_registration_without_screenshot(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('submit-event', args=[self.event_name])
        response = self.client.post(url, {
            'leader_name': 'Leader',
            'team_name': 'TeamX',
            'leader_email': 'leader@example.com',
            'leader_phone': '1234567890',
            'college': 'College',
            'year': '2024',
            'branch': 'Engineering',
            'team_members[]': ['Member1', 'Member2'],
            # 'screenshot' is omitted
        })
        self.assertEqual(response.status_code, 200)  # Should return to form with errors
        self.assertFalse(EventRegistration.objects.filter(team_name='TeamX').exists())
        self.assertContains(response, "Screenshot is required.")
