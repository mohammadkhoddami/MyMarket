from django import forms 
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'order_notes', )
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={'rows':5})
        }
        