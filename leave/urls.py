from django.contrib import admin
from django.urls import path
from .views import booked_leave, detail_view, create_leave

app_name = 'leave'

urlpatterns = [
    path('', booked_leave),
    path('<int:pk>/', detail_view),
    path('create/', create_leave)
]