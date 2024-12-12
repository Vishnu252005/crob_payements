from django.contrib import admin
from events.models import TeamMember, EventRegistration

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_registration']

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'team_name', 'screenshot']  # 'screenshot' is now mandatory