from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,2)]
# quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    override   = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)