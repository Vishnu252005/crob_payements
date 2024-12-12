from django.urls import path
from core.views import crob_home_view, event_page_view

urlpatterns = [
    path('crob-home/', crob_home_view, name='crob-home'),
    path('events/', event_page_view, name='events')

]