from django import forms
from .models import*
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User



class AgenceForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de l\'agence'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la ville'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la province'}),
            'commune': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez commune'}),
            'territoire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le territoire'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'adresse'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le numéro de téléphone'}),
            
        }

class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom du poste'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['agence','numero']  # Excluez 'agence' de la liste des champs du formulaire
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom'}),
            'postnom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le postnom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'adresse'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le quartier'}),
            'commune': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la commune'}),
            'activite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'activité'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le téléphone'}),
            'numero_national': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le numéro national'}),
            'carte_electeur': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_passeport': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        exclude = [
            'is_staff', 'last_name', 'first_name', 'password', 'last_login', 
            'is_superuser', 'groups', 'user_permissions', 'date_joined', 'is_active'
        ]  # Excluez les champs que vous ne voulez pas afficher dans le formulaire
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'adresse e-mail'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la date de naissance', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le lieu de naissance'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le numéro de téléphone'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'adresse'}),
            'agence': forms.Select(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }


class DepotForm(forms.ModelForm):
    class Meta:
        model = Carte
        fields = ['dateDepot', 'montant', 'motif', 'dateRetrait', 'client']  # Inclure tous les champs nécessaires
        widgets = {
            'dateDepot': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le montant'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'motif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le motif'}),
        }

class RetraitForm(forms.ModelForm):
    class Meta:
        model = Carte
        fields = ['dateRetrait', 'montant', 'motif', 'client']  # Inclure tous les champs nécessaires
        widgets = {
            'dateRetrait': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le montant'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'motif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le motif'}),
        }

 



class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",
                               max_length=32, help_text="<small id='emailHelp' class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label="",
                                 max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",
                                max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label="",
                             max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="", help_text="<small><ul class='form-text text-muted'><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>",
                                max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", help_text="<small class='form-text text-muted'>Enter the same password as before, for verification.</small>",
                                max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    username = forms.CharField(label="Username:",
                               max_length=32, help_text="<small id='emailHelp' class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name:",
                                 max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name:",
                                max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email",
                             max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="",
                               max_length=50, widget=forms.PasswordInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old password:",
                                   max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="New password:", 
                                    help_text="<small><ul class='form-text text-muted'><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>",
                                    max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="New password confirmation:",
                                    max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User

