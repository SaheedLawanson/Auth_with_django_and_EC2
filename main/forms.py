from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="listname", max_length = 200)
    check = forms.BooleanField(required=False) 