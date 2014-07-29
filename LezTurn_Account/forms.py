from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),
                               max_length=100)

class RegisterForm(forms.Form):
    username = forms.CharField(required=False,widget=forms.TextInput())
    email = forms.EmailField(required=False,widget=forms.TextInput())
    password = forms.CharField(required=False,widget=forms.PasswordInput)
    password_check = forms.CharField(required=False,widget=forms.PasswordInput)