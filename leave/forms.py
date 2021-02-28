
from django import forms
from .models import Leave
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()

class LeaveModelForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = (
            'leaveDate',
            'startTime',
            'endTime', 
            'staff'
        )

class LeaveForm(forms.Form):
    leave_date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'first_name')
        fields_classes = {'username':UsernameField}