from django import forms
from .models import *
from django.forms import ModelForm

class UserImageForm(forms.Form):
    image = forms.ImageField(label='Upload Image')


class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)

class addQuestionform(ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question here'}),
            'option1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 1'}),
            'option2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 2'}),
            'option3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 3'}),
            'option4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option 4'}),
            'correct_option': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correct option'}),
        }
        

class EncryptionForm(forms.Form):
    input_text = forms.CharField(label='Enter Plain Text', max_length=100)
    