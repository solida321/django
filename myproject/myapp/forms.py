from django import forms
from .models import Customer 

class customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','address']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter  name ',
                'id':'name',
                'name':'name'
            }),
            'address':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'write address'
            }),
        }

