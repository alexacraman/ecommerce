from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"})
        self.fields['last_name'].widget.attrs.update({'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"})
        self.fields['email'].widget.attrs.update({'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"})
        self.fields['address'].widget.attrs.update({'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"})
        self.fields['postal_code'].widget.attrs.update({'class': "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"})
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code']





