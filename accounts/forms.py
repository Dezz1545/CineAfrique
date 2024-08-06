from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    confirmation_mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'mot_de_passe']

    def clean(self):
        cleaned_data = super().clean()
        mot_de_passe = cleaned_data.get("mot_de_passe")
        confirmation_mot_de_passe = cleaned_data.get("confirmation_mot_de_passe")

        if mot_de_passe and confirmation_mot_de_passe:
            if mot_de_passe != confirmation_mot_de_passe:
                raise ValidationError("Les mots de passe ne correspondent pas.")
            if mot_de_passe.isdigit():
                raise ValidationError("Le mot de passe ne doit pas être uniquement composé de chiffres.")
        
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cet email est déjà utilisé.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ce nom d'utilisateur est déjà pris.")
        return username
    
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'sign__input', 'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'sign__input', 'placeholder': 'Mot de passe'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        

