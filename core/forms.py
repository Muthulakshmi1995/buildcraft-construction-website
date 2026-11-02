from django import forms
from .models import ContactMessage, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}

class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["name", "email", "phone", "project_type", "location", "budget", "details"]
        widgets = {"details": forms.Textarea(attrs={"rows": 4})}
