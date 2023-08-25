from django.urls import path
from .views import get_user_information_from_request

urlpatterns = [
    path('',get_user_information_from_request)
]