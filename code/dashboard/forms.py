from django import forms

from dashboard.models import UsersSystem


class UsersSystemForm(forms.ModelForm):

    class Meta:

        model = UsersSystem
        fields = [
                    'name',
                    'email',
                    'password',
                    'confirmation_password',
                    'office'
              ]
