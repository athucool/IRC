from django import forms
from .models import IRC_API
 
from django.contrib.auth import get_user_model
User = get_user_model()


class IRCForms(forms.ModelForm):
    
    class Meta():
        model=IRC_API
        fields = ('date_time','url',)
        widget={
            'date_time':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Y-M-D H:M *'}),
        }
   