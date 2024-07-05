from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']  # Fields to include from the Feedback model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})  # Apply Bootstrap form-control class
        self.fields['message'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
