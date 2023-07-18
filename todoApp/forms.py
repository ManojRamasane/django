from django import forms
from django.contrib.auth.models import User
from .models import CustomTodo

class CustomTodoForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    start_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    is_completed = forms.BooleanField(required=False)