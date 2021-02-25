from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Leave, Staff
from .forms import LeaveForm

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

def create_leave(request):
    form = LeaveForm()
    if request.method == "POST":
        print("recieving a post request")
        form  = LeaveForm(request.POST) 
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            leave_date = form.cleaned_data['leave_date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            staff = Staff.objects.first()
            Leave.objects.create(
                leaveDate = leave_date,
                startTime = start_time,
                endTime = end_time,
                staff = staff
            )
            print("Leave has been added")
            return redirect("/leave")
    context = {
        'forms': form
    }
    return render(request, 'leave/create_leave.html', context)