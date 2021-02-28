from django.contrib import admin
from django.urls import path
from .views import (
    booked_leave, detail_view, create_leave, update_leave, delete_leave, LeaveDetailView,
    LeaveListView, LeaveCreateView, LeaveUpdateView, LeaveDeleteView
)

app_name = 'leave'

urlpatterns = [
    path('', LeaveListView.as_view(), name='leave'),
    path('<int:pk>/', LeaveDetailView.as_view(), name='leave-detail'),
    path('<int:pk>/update/', LeaveUpdateView.as_view(), name='leave-update'),
    path('create/', LeaveCreateView.as_view(), name='leave-create'),
    path('<int:pk>/delete/', LeaveDeleteView.as_view(), name='leave-delete')
]