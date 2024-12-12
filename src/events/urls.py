from django.urls import path
from events.views import register_events_view, register_submission_view, payment_page_view, my_events_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register-event/<str:event_name>/', register_events_view, name='register-event'),
    path('submit-event/<str:event_name>/', register_submission_view, name='submit-event'),  # Added trailing slash for consistency
    path('my-events/', my_events_view, name='my-events'),
    path('payment-page/', payment_page_view, name='payment-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

