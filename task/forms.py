from django import forms
from .models import Task

class Taskforms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status', 'created_date', 'expiry_date', 'priority']
