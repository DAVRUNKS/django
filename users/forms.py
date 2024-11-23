from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Your Username"
        self.fields["username"].widget = forms.TextInput(attrs={"class": "form-control"})

        self.fields["email"].label = "Your Email"
        self.fields["email"].widget = forms.TextInput(attrs={"class": "form-control"})

        self.fields["password1"].label = "Your Password"
        self.fields["password1"].widget = forms.TextInput(attrs={"class": "form-control"})

        self.fields["password2"].label = "confirm Your Password"
        self.fields["password2"].widget = forms.TextInput(attrs={"class": "form-control"})

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Your Username"
        self.fields["username"].widget = forms.TextInput(attrs={"class": "form-control"})

        self.fields["password"].label = "Your password"
        self.fields["password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
