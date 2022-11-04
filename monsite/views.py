from django.http import HttpResponse

# Les vues prennent une requête http en entrée et retourne une requête http
def toto(request):
    return HttpResponse("Toto")

# Les paramètres captés dans les urls doivent être précisés dans la vue
def article_annee_mois(request, annee, mois):
    return HttpResponse(f"{annee} {mois}")