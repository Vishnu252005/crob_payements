from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)  
    event_registration = models.ForeignKey('EventRegistration', on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return f"{self.name} ({self.event_registration.team_name})"


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_registrations',  null=True,)
    event_name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    leader_name = models.CharField(max_length=100)
    leader_email = models.EmailField()
    leader_phone = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    team_members = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to='screenshots/', blank=False, null=False, default='screenshots/default.png')  # Added default

    def __str__(self):
        return f"{self.event_name} - {self.team_name}"

@receiver(post_save, sender=TeamMember)
@receiver(post_delete, sender=TeamMember)
def update_team_member_names(sender, instance, **kwargs):
    event_registration = instance.event_registration
    
    event_registration.team_members = ', '.join(
        member.name for member in event_registration.members.all()  
    )
    event_registration.save()