from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'appFamilyReuion'




urlpatterns = [
    path('',views.dashboard, name='dashboard'),  
    # URLs pour Agence
  
    path('create_agence/', views.create_agence, name='create_agence'),
    path('edit_agence/<int:id>/', views.edit_agence, name='edit_agence'),
    path('update_agence/<int:id>/', views.update_agence, name='update_agence'),
    path('delete_agence/<int:id>/', views.delete_agence, name='delete_agence'),
    path('show_agences/', views.show_agences, name='show_agences'),

    # URLs pour Poste
    path('create_poste/', views.create_poste, name='create_poste'),
    path('edit_poste/<int:id>/', views.edit_poste, name='edit_poste'),
    path('update_poste/<int:id>/', views.update_poste, name='update_poste'),
    path('delete_poste/<int:id>/', views.delete_poste, name='delete_poste'),
    path('show_postes/', views.show_postes, name='show_postes'),

    # URLs pour Personnel
    path('create_personnel/', views.create_personnel, name='create_personnel'),
    path('edit_personnel/<int:id>/', views.edit_personnel, name='edit_personnel'),
    path('update_personnel/<int:id>/', views.update_personnel, name='update_personnel'),
    path('delete_personnel/<int:id>/', views.delete_personnel, name='delete_personnel'),
    path('show_personnel/', views.show_personnel, name='show_personnel'),

    # URLs pour Client
    path('create_client/', views.create_client, name='create_client'),
    path('edit_client/<int:id>/', views.edit_client, name='edit_client'),
    path('update_client/<int:id>/', views.update_client, name='update_client'),
    path('delete_client/<int:id>/', views.delete_client, name='delete_client'),
    path('show_clients/', views.show_clients, name='show_clients'),
    path('detail_client/<int:id>/',views.detail_clients,name='detail_client'),
        # URLs pour Carte
    path('create_carte/', views.create_carte, name='create_carte'),
    path('edit_carte/<int:id>/', views.edit_carte, name='edit_carte'),
    path('update_carte/<int:id>/', views.update_carte, name='update_carte'),
    path('delete_carte/<int:id>/', views.delete_carte, name='delete_carte'),
    path('show_cartes/', views.show_cartes, name='show_cartes'),

    # URL pour la recherche de clients
    path('search_clients/', views.search_clients, name='search_clients'),

    path('accounts/login/', views.login_user, name='accounts/login/'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]