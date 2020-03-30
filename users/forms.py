from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Operator
from random import randint


class Register_form(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_operator = True
        if commit:
            user.save()
            Op = Operator()
            Op.operator_id = user.username + 'ID' + str(randint(1, 100))
            Op.save()
        return user