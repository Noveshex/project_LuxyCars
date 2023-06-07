from django import forms
from django.core.exceptions import ValidationError

from .models import *


class GetContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'inputBox'}),
            'name': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            # 'phone': forms.TextInput(attrs={'class': 'inputBox'}),
            'phone': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            # 'email': forms.TextInput(attrs={'class': 'inputBox'}),
            'email': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
            'message': forms.Textarea(attrs={'cols': 100, 'rows': 2}),
        }