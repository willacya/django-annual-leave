from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Leave, Staff
from .forms import LeaveForm, LeaveModelForm
from django.views.generic import TemplateView, CreateView ,UpdateView, DeleteView, ListView, DetailView

class LandingPageView(TemplateView):
    template_name = 'landing.html'

def landing_page(request):
    return render(request, 'landing.html')
# Create your views here.

class LeaveListView(ListView):
    template_name = 'leave/booked.html'
    queryset = Leave.objects.all()
    context_object_name = 'leave'


def booked_leave(request):
    leave = Leave.objects.all()
    context = {
        
        'leave':leave

    }
    return render(request, "leave/booked.html", context)

class LeaveDetailView(DetailView):
    template_name = 'leave/leave_detail.html'
    queryset = Leave.objects.all()
    context_object_name = 'leave'


def detail_view(request, pk):
    leave = Leave.objects.get(id=pk)
    context = {
        
        'leave':leave

        }
    return render(request, 'leave/leave_detail.html', context)

class LeaveCreateView(CreateView):
    template_name = 'leave/create_leave.html'
    form_class = LeaveModelForm

    def get_success_url(self):
        return reverse("leave:leave")

def create_leave(request):
    form = LeaveModelForm()
    if request.method == "POST":
        print("recieving a post request")
        form  = LeaveModelForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("/leave")
    context = {
        'forms': form
    }
    return render(request, 'leave/create_leave.html', context)

class LeaveUpdateView(UpdateView):
    template_name = 'leave/update_leave.html'
    queryset = Leave.objects.all()
    form_class = LeaveModelForm

    def get_success_url(self):
        return reverse('leave:leave')

def update_leave(request, pk):
    leave = Leave.objects.get(id=pk)
    form = LeaveModelForm(instance=leave)
    if request.method == "POST":
        form = LeaveModelForm(request.POST, instance=leave) 
        if form.is_valid():
            form.save()
            return redirect("/leave")
    context = {
        'form': form,
        'leave': leave
    }
    return render(request, 'leave/update_leave.html', context)

class LeaveDeleteView(DeleteView):
    template_name = 'leave/delete_leave.html'
    queryset = Leave.objects.all()

    def get_success_url(self):
        return reverse("leave:leave")

def delete_leave(request, pk):
    leave = Leave.objects.get(id=pk)
    leave.delete()
    return redirect("/leave")
# def update_leave(request, pk):
#     leave = Leave.objects.get(id=pk)
#     form = LeaveForm()
#     if request.method == "POST":
#         form  = LeaveModelForm(request.POST) 
#         if form.is_valid():
#             leave_date = form.cleaned_data['leave_date']
#             start_time = form.cleaned_data['start_time']
#             end_time = form.cleaned_data['end_time']
#             staff = Staff.objects.first()
#             leave.leaveDate = leave_date
#             leave.startTime = start_time
#             leave.endTime = end_time
#             lead.save()
#             return redirect("/leave")
    # context = {
    #     'forms': form,
    #     'leave': leave
    # }
    # return render(request, 'leave/update_leave.html', context)


    # def create_leave(request):
    # form = LeaveModelForm()
    # if request.method == "POST":
    #     print("recieving a post request")
    #     form  = LeaveModelForm(request.POST) 
    #     if form.is_valid():
    #         print("form is valid")
    #         print(form.cleaned_data)
    #         leave_date = form.cleaned_data['leave_date']
    #         start_time = form.cleaned_data['start_time']
    #         end_time = form.cleaned_data['end_time']
    #         staff = Staff.objects.first()
    #         Leave.objects.create(
    #             leaveDate = leave_date,
    #             startTime = start_time,
    #             endTime = end_time,
    #             staff = staff
    #         )
    #         print("Leave has been added")
    #         return redirect("/leave")
    # context = {
    #     'forms': form
    # }
    # return render(request, 'leave/create_leave.html', context)