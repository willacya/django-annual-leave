
from django import forms

class LeaveForm(forms.Form):
    leave_date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
