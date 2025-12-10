from django import forms
from .models import Contact

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'subject', 'message']
#         widgets = {
#             'message': forms.Textarea(attrs={'rows': 5}),
#         }



class ContactForm(forms.ModelForm):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
