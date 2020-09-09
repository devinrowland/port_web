from django import forms

from .models import EmailEntry

class EmailEntryForm(forms.ModelForm):
    class Meta:
        model = EmailEntry
        fields = ['email']
    
    #validating email if they have already registered
    def clean_email(self): #clean_<field_name>
        email = self.cleaned_data.get("email")
        qs = EmailEntry.objects.filter(email__iexact=email) #abcW@gmail.com = abcw@gmail.com
        if qs.exists():
            raise forms.ValidationError("Thank you, you have already registered.")