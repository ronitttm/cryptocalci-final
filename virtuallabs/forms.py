from django import forms
from .models import *
from django.forms import ModelForm

class UserImageForm(forms.Form):
    image = forms.ImageField(label='Upload Image')


class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"