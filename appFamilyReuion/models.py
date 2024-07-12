from django.db import models
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = Personnel(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class Agence(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    territoire = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)


    def __str__(self):
        return self.nom

class Poste(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



def generate_numero():
    # Génère un numéro aléatoire de 12 caractères au format xxxx-xxxx-xxxx
    return '{}-{}-{}'.format(
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    )

class Personnel(AbstractUser):
    USER_TYPE = ((1, "Admin"), (2, "Gestionnaire"), (3, "Utilisateur"))
    SEXE = [("M", "Masculin"), ("F", "Feminin")]

    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, null=True)
    sexe = models.CharField(max_length=1, choices=SEXE)
    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=256, blank=True, null=True)
    telephone = models.CharField(max_length=256, blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    agence = models.ForeignKey('Agence', on_delete=models.CASCADE, related_name='personnels',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.nom.upper()} {self.prenom.capitalize()}"


class Client(models.Model):
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    quartier = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    numero = models.CharField(max_length=12, unique=True, blank=True)
    activite = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    numero_national = models.CharField(max_length=16)
    carte_electeur = models.ImageField(upload_to='carte_electeur')
    photo_passeport = models.ImageField(upload_to='photo_passeport')
    agence = models.ForeignKey('Agence', on_delete=models.CASCADE, related_name='clients')

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = generate_numero()
        super(Client, self).save(*args, **kwargs)


class Carte(models.Model):
    dateDepot = models.DateField(blank=True, null=True)
    dateRetrait = models.DateField(blank=True, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    motif = models.CharField(max_length=20, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cartes')

    def __str__(self):
        return self.montant
