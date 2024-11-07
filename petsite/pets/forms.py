from django import forms
from .models import PetUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = PetUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields must be a dictionary structure, so can't do f.widget, f.label, etc
        for f in self.fields:
            # set each field's placeholder text to its name
            self.fields[f].widget.attrs.update({'placeholder': self.fields[f].label})
