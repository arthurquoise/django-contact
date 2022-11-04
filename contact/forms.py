import datetime
from django import forms

# Création d'une classe héritant de Form
class ContactForm(forms.Form):
    # Utilisation des méthodes de forms pour définir les champs du formulaire
    firstname = forms.CharField(label="First name", max_length=150)
    lastname = forms.CharField(label="Last name", max_length=150)
    birth_date = forms.DateField(label="Date of birth", initial=datetime.date.today)
    phone = forms.CharField(label="Phone", max_length=10)
    email = forms.CharField(label="Email", max_length=150)