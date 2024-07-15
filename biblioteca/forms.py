from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from django import forms
from .models import Servicio
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Servicio

# Formulario de creación de usuario
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Formulario de autenticación
class AutForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

    class Meta:
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(AutForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['password'].label = "Contraseña"

# Formulario para cambiar el perfil del usuario
class PerfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields.pop('password', None)  # Elimina el campo 'password' del formulario
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})

# Formulario para registrar un nuevo usuario
class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CambiarContrasenaForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza los widgets o añade clases CSS aquí si es necesario
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña actual'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nueva contraseña'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar nueva contraseña'
        })

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['servicio', 'precio', 'categoria', 'imagen']
        labels ={
            'servicio':'Servicio',
            'precio' : 'Precio',
            'categoria':'Categoria',
            'imagen':'Imagen'
        }
        widgets={

            'servicio':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese Nombre del Servicio',
                    'id': 'servicio',
                    'class': 'form-control',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese Precio del Servicio',
                    'id':'precio',
                    'class':'form-control',
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese la categoria del Servicio',
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            )
        }
  