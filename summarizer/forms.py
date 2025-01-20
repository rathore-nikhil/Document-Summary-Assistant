from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('uploaded_file',)
        
class DocumentForm(forms.ModelForm):
    SUMMARY_LENGTH_CHOICES = [
        ('short', 'Short'),
        ('medium', 'Medium'),
        ('long', 'Long'),
    ]
    summary_length = forms.ChoiceField(choices=SUMMARY_LENGTH_CHOICES, required=True)

    class Meta:
        model = Document
        fields = ('uploaded_file', 'summary_length',)
