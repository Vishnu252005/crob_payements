from django.urls import path
from directory.views import account_profile_view

urlpatterns = [
    path('profile-page/', account_profile_view, name='profile-page'),
]