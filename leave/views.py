from django.shortcuts import render
from django.http import HttpResponse
from .models import Leave

# Create your views here.
def booked_leave(request):
    leave = Leave.objects.all()
    context = {
        
        'leave':leave

    }
    return render(request, "leave/booked.html", context)

def detail_view(request, pk):
    leave = Leave.objects.get(id=pk)
    context = {
        
        'leave':leave

        }
    return render(request, 'leave/leave_detail.html', context)