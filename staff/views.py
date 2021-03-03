from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from leave.models import Staff
from .forms import StaffModelForm
from .mixins import OrganisorAndLoginRequiredMixin

# Create your views here.
class StaffListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'staff/staff_list.html'
    
    def get_queryset(self):
        return Staff.objects.all()

class StaffCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'staff/staff_create.html'
    form_class = StaffModelForm
    
    def get_success_url(self):
        return reverse("staff:staff-list")

    def form_valid(self, form):
        staff = form.save(commit=False)
        staff.organisation = self.request.user.userprofile
        staff.save()
        return super(StaffCreateView, self).form_valid(form)

class StaffDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'staff/staff_detail.html'
    context_object_name = "staff"

    def get_queryset(self):
        return Staff.objects.all()

class StaffUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'staff/staff_update.html'
    form_class = StaffModelForm
    context_object_name = "staff"

    def get_queryset(self):
        return Staff.objects.all()

    def get_success_url(self):
        return reverse("staff:staff-list")

class StaffDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'staff/staff_delete.html'
    context_object_name = 'staff'

    def get_queryset(self):
        return Staff.objects.all()

    def get_success_url(self):
        return reverse("staff:staff-list")