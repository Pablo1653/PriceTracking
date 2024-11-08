from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Formulario de creación de usuario personalizado
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        help_text="Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.",
        max_length=150
    )
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        help_text="Introduce una dirección de correo electrónico válida.",
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text=(  # Aquí está la ayuda que debe dar indicaciones claras a los usuarios.
            "La contraseña no debe ser demasiado similar a tu información personal. "
            "Debe contener al menos 8 caracteres, no ser una contraseña común y no ser completamente numérica."
        ),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        help_text="Introduce la misma contraseña que antes, para verificación.",
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

# Formulario de inicio de sesión
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )
