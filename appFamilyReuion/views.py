from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from django.contrib import messages
from .models import Agence, Poste, Personnel, Client, Carte
from .forms import *


from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import login_required


# Create your views here.

@login_required
def dashboard(request, *args, **kwargs):
    total_clients = Client.objects.count()
    total_agences = Agence.objects.count()
    total_personnels = Personnel.objects.count()
    total_cartes = Carte.objects.count()
  

    return render(request, 'index.html',{
        'total_clients': total_clients,
        'total_agences': total_agences,
        'total_personnels': total_personnels,
        'total_cartes': total_cartes
        })


# Dans views.py 







# Pour Agence##################################################################################

def create_agence(request):
    if request.method == "POST":
        form = AgenceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Agence créée avec succès!")
                return redirect('/show_agences/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création de l'agence!")
    else:
        form = AgenceForm()  # Si la requête n'est pas POST, créez simplement une nouvelle instance du formulaire

    return render(request, 'pages/agences/show_agences.html', {'form': form})

def show_agences(request):
    agences = Agence.objects.all()
    form = AgenceForm()
    return render(request, 'pages/agences/show_agences.html', {'agences': agences, 'form': form})


def edit_agence(request, id):
    agence = get_object_or_404(Agence, id=id)
    form = AgenceForm(instance=agence)
    form_data = model_to_dict(form.instance)  # Convertir l'instance de modèle en dictionnaire
    return JsonResponse(form_data)

def update_agence(request, id):
    agence = get_object_or_404(Agence, id=id)
    form = AgenceForm(request.POST or None, instance=agence)
    if form.is_valid():
        form.save()
        messages.success(request, 'Agence mise à jour avec succès!')
        return redirect('/show_agences/')
    return render(request, 'pages/agences/show_agences.html', {'form': form, 'agence': agence})

def agence_update(request, agenceId=None):
    agence = get_object_or_404(Agence, pk=agenceId) if agenceId else None

    if request.method == 'POST':
        form = AgenceForm(request.POST, instance=agence)
        if form.is_valid():
            form.save()
            return redirect('/show_agences/')  # Remplacez 'nom_de_votre_vue_liste_agences' par le nom de votre vue qui affiche la liste des agences
    else:
        form = AgenceForm(instance=agence)

    return render(request, 'pages/agences/show_agences.html', {'form': form})  

def delete_agence(request, id):
    agence = get_object_or_404(Agence, id=id)
    agence.delete()
    messages.success(request, 'Agence supprimée avec succès!')
    return redirect('/show_agences/')
# Pour Agence##################################################################################

# Pour Poste ##################################################################################

    
def create_poste(request):
    if request.method == "POST":
        form = PosteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Poste créé avec succès!")
                return redirect('/show_postes/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création de l'agence!")
    else:
        form = PosteForm()  # Si la requête n'est pas POST, créez simplement une nouvelle instance du formulaire

    return render(request, 'pages/poste/poste.html', {'form': form})

def show_postes(request):
    postes = Poste.objects.all()
    form = PosteForm()
    return render(request, 'pages/poste/poste.html', {'postes': postes, 'form': form})


def edit_poste(request, id):
    poste = get_object_or_404(Poste, id=id)
    form = PosteForm(instance=poste)
    form_data = model_to_dict(form.instance)  # Convertir l'instance de modèle en dictionnaire
    return JsonResponse(form_data)


def update_poste(request, id):
    poste = get_object_or_404(Poste, id=id)
    form = PosteForm(request.POST or None, instance=poste)
    if form.is_valid():
        form.save()
        messages.success(request, 'Poste mis à jour avec succès!')
        return redirect('/show_postes/')
    return render(request, 'pages/poste/poste.html', {'form': form, 'poste': poste})

def delete_poste(request, id):
    poste = get_object_or_404(Poste, id=id)
    poste.delete()
    messages.success(request, 'Poste supprimé avec succès!')
    return redirect('/show_postes/')
# Pour Poste ##################################################################################

# Pour Personnel ##################################################################################

def create_personnel(request):
    if request.method == "POST":
        form = PersonnelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Personnel créé avec succès!")
                return redirect('/show_personnel/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création du commissariat!")
    else:
        form = PersonnelForm()

    return render(request, 'pages/personnel/personnel.html', {'form': form})

def show_personnel(request):
    personnels = Personnel.objects.all()
    form = PersonnelForm()
    return render(request, 'pages/personnel/personnel.html', {'personnels': personnels ,'form': form})


def edit_personnel(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    form = PersonnelForm(instance=personnel)
    form_data = model_to_dict(form.instance, exclude=['profile_pic'])  # Exclure le champ 'profile_pic'
    return JsonResponse(form_data)


def update_personnel(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    form = PersonnelForm(request.POST or None, instance=personnel)
    if form.is_valid():
        form.save()
        messages.success(request, 'Personnel mis à jour avec succès!')
        return redirect('/show_personnel/')
    return render(request, 'pages/personnel/personnel.html', {'form': form, 'personnel': personnel})

def delete_personnel(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    personnel.delete()
    messages.success(request, 'Personnel supprimé avec succès!')
    return redirect('/show_personnel/')
# Pour Personnel ##################################################################################

# Pour Client ##################################################################################


@login_required
def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save(commit=False)
            client.agence = request.user.agence 
            print(client.agence) # Assignez l'agence de l'utilisateur connecté
            try:
                client.save()
                messages.success(request, "Client créé avec succès!")
                return redirect('/show_clients/')
            except Exception as e:
                print(form.errors)
                messages.error(request, f"Erreur lors de la création du client : {e}")
        else:
            print(form.errors)
            messages.error(request, "Formulaire invalide. Veuillez vérifier les données.")
    else:
        form = ClientForm()

    return render(request, 'pages/client/client.html', {'form': form})


def show_clients(request):
    clients = Client.objects.all()
    form = ClientForm()
    return render(request, 'pages/client/client.html', {'clients': clients,'form': form})

def detail_clients(request, id):
    clients = get_object_or_404(Client, id=id)
    form = ClientForm()
    cardForm = RetraitForm()
    cardForm = DepotForm()
    return render(request, 'pages/client/detailClient.html', {'clients': clients,'form': form,'cardForm':cardForm})

 
def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(instance=client)
    form_data = model_to_dict(form.instance)  # Convertir l'instance de modèle en dictionnaire
    return JsonResponse(form_data)

def update_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)
    if form.is_valid():
        form.save()
        messages.success(request, 'Client mis à jour avec succès!')
        return redirect('/show_clients/')
    return render(request, 'pages/client/client.html', {'form': form, 'client': client})

def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    messages.success(request, 'Client supprimé avec succès!')
    return redirect('/show_clients/')

def search_clients(request):
    query = request.GET.get('q')
    clients = None
    
    if query:
        clients = Client.objects.filter(nom__icontains=query)  # Recherche par nom, vous pouvez ajuster selon vos besoins
    
    return render(request, 'search_clients.html', {'clients': clients, 'query': query})
# Pour Client ##################################################################################

# Pour Carte ##################################################################################
"""
def create_carte(request):
    form = CarteForm()
    if request.method == "POST":
        form = CarteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Carte créée avec succès!")
                return redirect('/show_cartes')
            except:
                messages.error(request, "Quelque chose s'est mal passé!")
                form = CarteForm()
    return render(request, 'pages/carte/carte.html', {'form': form})
"""
def show_cartes(request):
    cartes = Carte.objects.all() 
    form = DepotForm()
    return render(request, 'pages/carte/carte.html', {'cartes': cartes,'form': form})

def edit_carte(request, id):
    carte = get_object_or_404(Carte, id=id)
    form = DepotForm(instance=carte)
    form_data = model_to_dict(form.instance)  # Convertir l'instance de modèle en dictionnaire
    return JsonResponse(form_data)
"""
def update_carte(request, id):
    carte = get_object_or_404(Carte, id=id)
    form = CarteForm(request.POST or None, instance=carte)
    if form.is_valid():
        form.save()
        messages.success(request, 'Carte mise à jour avec succès!')
        return redirect('/show_cartes')
    return render(request, 'pages/carte/carte.html', {'form': form, 'carte': carte})
"""
def delete_carte(request, id):
    carte = get_object_or_404(Carte, id=id)
    carte.delete()
    messages.success(request, 'Carte supprimée avec succès!')
    return redirect('/show_cartes')





def create_carte(request):
    if request.method == "POST":
        form = DepotForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Carte créée avec succès!")
                return redirect('/show_cartes/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création de la carte!")


    return render(request, 'pages/carte/carte.html', {'form': form})

def update_carte(request, id):
    carte = get_object_or_404(Carte, id=id)
    if request.method == "POST":
        form = RetraitForm(request.POST, instance=carte)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carte mise à jour avec succès!')
            return redirect('/show_cartes/')
    
    return render(request, 'pages/carte/carte.html', {'form': form, 'carte': carte})












# Pour Carte ##################################################################################






def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('/')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('/accounts/login/')
    else:
        return render(request, 'pages/examples/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/accounts/login/')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/examples/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'pages/examples/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect('/')
    else:
        form = ChangePasswordForm(user=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'pages/examples/change_password.html', context)


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "User créé avec succès!")
                return redirect('/show_users/')
            except:
                messages.error(request, "Quelque chose s'est mal passé lors de la création de l'utilisateur!")
    else:
        form = UserForm()
    return render(request, 'pages/personnel/personnel.html', {'form': form})
