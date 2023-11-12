from django import forms
from django.utils.safestring import mark_safe

class DeleteUserForm(forms.Form):
    delete_checkbox = forms.BooleanField(label=mark_safe('Are you sure you want to delete your account?'), required=True)
    def __init__(self, *args, **kwargs):
        super(DeleteUserForm, self).__init__(*args, **kwargs)