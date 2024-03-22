from django import forms

class UserImageForm(forms.Form):
    image = forms.ImageField(label='Upload Image')


class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)