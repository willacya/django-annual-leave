from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Leave, Staff
from .forms import LeaveForm, LeaveModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, CreateView ,UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from staff.mixins import OrganisorAndLoginRequiredMixin


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(TemplateView):
    template_name = 'landing.html'

def landing_page(request):
    return render(request, 'landing.html')
# Create your views here.

class LeaveListView(LoginRequiredMixin, ListView):
    template_name = 'leave/booked.html'
    queryset = Leave.objects.all()
    context_object_name = 'leave'


def booked_leave(request):
    leave = Leave.objects.all()
    context = {
        
        'leave':leave

    }
    return render(request, "leave/booked.html", context)

class LeaveDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leave/leave_detail.html'
    queryset = Leave.objects.all()
    context_object_name = 'leave'


def detail_view(request, pk):
    leave = Leave.objects.get(id=pk)
    context = {
        
        'leave':leave

        }
    return render(request, 'leave/leave_detail.html', context)

class LeaveCreateView(OrganisorAndLoginRequiredMixin,CreateView):
    template_name = 'leave/create_leave.html'
    form_class = LeaveModelForm

    def get_success_url(self):
        return reverse("leave:leave")

    def form_valid(self, form):
        send_mail(
            subject='A leave date has been added', 
            message='Go to the site to see the new leave',
            from_email = "test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(LeaveCreateView, self).form_valid(form)

def create_leave(request):
    form = LeaveModelForm()
    if request.method == "POST":
        print("recieving a post request")
        form  = LeaveModelForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("/leave")
    context = {
        'form': form
    }
    return render(request, 'leave/create_leave.html', context)

class LeaveUpdateView(LoginRequiredMixin,UpdateView):
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

class LeaveDeleteView(LoginRequiredMixin,DeleteView):
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