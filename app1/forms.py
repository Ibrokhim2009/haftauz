from django import forms
from app1.models import Contact




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','massage']