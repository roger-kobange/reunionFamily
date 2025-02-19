# Generated by Django 4.2 on 2024-06-24 16:04

import appFamilyReuion.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=50)),
                ('territoire', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('postnom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('quartier', models.CharField(max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('numero', models.CharField(blank=True, max_length=12, unique=True)),
                ('activite', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_national', models.CharField(max_length=16)),
                ('carte_electeur', models.ImageField(upload_to='carte_electeur')),
                ('photo_passeport', models.ImageField(upload_to='photo_passeport')),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='appFamilyReuion.agence')),
            ],
        ),
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDepot', models.DateField(blank=True, null=True)),
                ('dateRetrait', models.DateField(blank=True, null=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('motif', models.CharField(blank=True, max_length=20, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartes', to='appFamilyReuion.client')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Gestionnaire'), (3, 'Utilisateur')])),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('nom', models.CharField(max_length=256)),
                ('prenom', models.CharField(max_length=256)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('lieu_naissance', models.CharField(blank=True, max_length=256, null=True)),
                ('telephone', models.CharField(blank=True, max_length=256, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnels', to='appFamilyReuion.agence')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', appFamilyReuion.models.CustomUserManager()),
            ],
        ),
    ]
