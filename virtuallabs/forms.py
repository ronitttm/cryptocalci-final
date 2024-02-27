from django import forms
from .models import UserImage

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)