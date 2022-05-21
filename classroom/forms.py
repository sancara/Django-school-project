from email import message
from socket import fromshare
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()