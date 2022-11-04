from django.urls import path
from . import views
# Afficher les contacts
# Afficher la fiche du contact
# Créer un contact
# Modifier un contact
# Supprimer les contacts

app_name = 'contact'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('person/<int:id>', views.contact_detail, name='contact_detail'),
    path('person/new', views.contact_new, name='contact_new'),
    path('person/<int:id>/edit', views.contact_edit, name='contact_edit'),
    path('person/<int:id>/delete', views.contact_delete, name='contact_delete'),
]