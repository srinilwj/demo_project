from .models import Signup
from django import forms
from django.forms import ModelForm

class Signupform(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    email_address = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Signup
        fields = "__all__"


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password mismatch")
        return confirm_password



class Loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email_address = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)