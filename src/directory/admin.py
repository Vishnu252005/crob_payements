from django.contrib import admin
from directory.models import Profile

@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['user']