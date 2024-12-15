from django.urls import path
from events.views import register_events_view, register_submission_view, payment_page_view, my_events_view

urlpatterns = [
    path('register-event/<str:event_name>/', register_events_view, name='register-event'),
    path('submit-event/<str:event_name>/', register_submission_view, name='submit-event'), 
    path('my-events/', my_events_view, name='my-events'),
    path('payment-page/', payment_page_view, name='payment-page'),
]


