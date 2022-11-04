"""monsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import settings
from . import views
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Liste permettant de définir les routes de notre application
urlpatterns = [
    # path prend en paramètres (obligatoires) la route et la vue associée
    # path("admin/", admin.site.urls),
    path("toto", views.toto, name="toto"),
    # Il est possible de capturer les paramètres dans nos URLs avec les chevrons
    path('articles/<int:annee>/<slug:mois>', views.article_annee_mois, name="article"),
    path('contact/', include('contact.urls')),
    path('', RedirectView.as_view(url='contact/', permanent=True))

]

# On ajoute les fichiers statiques aux URLs
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)