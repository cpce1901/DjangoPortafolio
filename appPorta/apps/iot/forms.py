from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario",
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingresa usuario",
                "class": "text-input",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ingresa contraseña",
                "class": "text-input",
            }
        ),
    )


