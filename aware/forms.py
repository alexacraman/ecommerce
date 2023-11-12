from django import forms
class ContactForm(forms.Form):
    # error_css_class = 'error'
    # required_css_class = 'required'
    name = forms.CharField(max_length=255,
        widget=forms.TextInput(
            attrs={'class': 'bg-blue-50 rounded border-2 border-slate-400 p-2 my-2 text-sm w-full block'}
        )
    )
    email = forms.EmailField(max_length=255,
        widget=forms.EmailInput(
            attrs={'class': 'bg-blue-50 rounded border-2 border-slate-400 p-2 my-2 text-sm w-full block'}
        )
    )
    message = forms.CharField(max_length=500,
        widget=forms.Textarea(
            attrs={'class': 'bg-blue-50 rounded border-2 border-slate-400 p-2 my-2 text-sm w-full block', 'rows': 3, 'cols': 19}
        )
    )
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'class': 'bg-blue-50 rounded border-2 border-slate-400 p-2 my-2 text-sm w-full block'})
    #     self.fields['email'].widget.attrs.update({'class': 'bg-blue-50 rounded border-2 border-slate-400 p-2 my-2 text-sm w-full block'})
    #     self.fields['message'].widget.attrs.update({'class': 'bg-blue-50 rounded border-2 border-slate-400 p-2 my-2 text-sm w-full block'})