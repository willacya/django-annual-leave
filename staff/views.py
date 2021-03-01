from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from leave.models import Staff
from .forms import StaffModelForm

# Create your views here.
class StaffListView(LoginRequiredMixin, generic.ListView):
    template_name = 'staff/staff_list.html'
    
    def get_queryset(self):
        return Staff.objects.all()

class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'staff/staff_create.html'
    form_class = StaffModelForm
    
    def get_success_url(self):
        return reverse("staff:staff-list")

    def form_valid(self, form):
        staff = form.save(commit=False)
        staff.organisation = self.request.user.userprofile
        staff.save()
        return super(StaffCreateView, self).form_valid(form)