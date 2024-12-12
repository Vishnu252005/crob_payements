from django import forms
from events.models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = [
            'team_name', 'leader_name', 'leader_email',
            'leader_phone', 'college', 'year', 'branch', 'screenshot'
        ]
        widgets = {
            'screenshot': forms.ClearableFileInput(attrs={'required': True}),
        }