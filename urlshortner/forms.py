from django import forms
from .models import URL

class URLforms(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']