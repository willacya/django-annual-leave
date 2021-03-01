from leave.models import Staff
from django import forms

class StaffModelForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = {
        'user',
        }