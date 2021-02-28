
from django import forms
from .models import Leave

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
