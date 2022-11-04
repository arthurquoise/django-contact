from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

from .models.contact import Contact

# Retourne la liste des contacts
def contact_list(request):
    contacts = []
    contacts = Contact.get_all_contacts()
    context = {'contacts': contacts, 'count': len(contacts)}
    return render(request, 'contact/contact-list.html', context)

# Affiche la fiche détaillée d'un contact
def contact_detail(request, id):

    contact = Contact.get_contact_by_id(id)

    if(contact):
        return render(request, 'contact/contact-detail.html', {'contact': contact})
    else:
        return HttpResponseNotFound(f"<h1> Aucun contact trouvé avec l'id : {id} </h1>")

# Créer un nouveau contact
def contact_new(request):

    # On envoie des données depuis le formulaire du template HTML
    if(request.method == 'POST'):
        # On instancie l'objet ContactForm avec les données du formulaire
        form = ContactForm(request.POST)
        # Vérification des données du formulaire
        if(form.is_valid()):
            # Transformation des données en dictionnaire en les nettoyant
            cd = form.cleaned_data
            contact = Contact(None, cd.get('firstname'), cd.get('lastname'), cd.get('birth_date'), cd.get('phone'), cd.get('email'))
            if(Contact.add_contact(contact)):
                return redirect('/')
    else:
        # Par défaut, la méthode est GET, on renvoie un formulaire vide
        form = ContactForm()

    return render(request, 'contact/contact-edit.html', {'form': form})

# Met à jour le contact
def contact_edit(request, id):
    contact = Contact.get_contact_by_id(id)

    # On vérifie que le contact existe
    if(not contact):
        HttpResponseNotFound(f"<h1> Aucun contact trouvé avec l'id : {id} </h1>")

    # Mise à jour du contact à l'aide du formulaire
    if(request.method == 'POST'):
        form = ContactForm(request.POST)
        if(form.is_valid()):
            cd = form.cleaned_data
            contact = Contact(id, cd.get('firstname'), cd.get('lastname'), cd.get('birth_date'), cd.get('phone'), cd.get('email'))
            if(Contact.update_contact(contact)):
                return redirect('/')
    # On charge les données du contact dans le formulaire
    else:
        form = ContactForm(data=contact.__dict__)
    
    return render(request, 'contact/contact-edit.html', {'form': form})

# Supression d'un contact par son identifiant unique
def contact_delete(request, id):
    if(Contact.delete_contact(id)):
        return redirect('/')
    else:
        return HttpResponseNotFound(f"<h1> Problème rencontré lors de la suppression du contact avec l'id : {id} </h1>")
