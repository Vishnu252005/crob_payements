from django.urls import path
from authentication.views import login_user_view, logout_user, register_user_view

urlpatterns = [
    path('register/', register_user_view, name='register'),
    path('login/', login_user_view, name='login'),
    path('logout/', logout_user, name='logout')
]