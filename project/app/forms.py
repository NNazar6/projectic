from django import forms


class UserForm(forms.Form):
    email = forms.CharField(required=False, min_length=5, max_length=101000,
                           label='Enter you email', help_text='HEllO',
                           widget=forms.TextInput(attrs={'class': 'myclass'}))
    password = forms.IntegerField(min_value=4, max_value=8,
                             widget=forms.PasswordInput(attrs={'class': 'myclass',}))
class LogForm(forms.Form):
    name = forms.CharField(required=False,
                           label='Enter you name',
                           widget=forms.TextInput(attrs={'class': 'myclass',
                                                         'placeholder': 'Ivan'}))
    email = forms.EmailField(required=False, min_length=5, max_length=100,
                            label='Enter you email', help_text='HEllO',
                            widget=forms.EmailInput(attrs={'class': 'myclass',
                                                           'placeholder': 'ivanov_ivan@gmail.ru'}))
    password = forms.IntegerField(min_value=4, max_value=100,
                                widget=forms.PasswordInput(attrs={'class': 'myclass',}))

