from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import OffreVoyage

def login(request):
    # Si l'utilisateur est déjà connecté, redirigez-le directement vers la liste des offres
    if request.user.is_authenticated:
        return redirect('offres_list')

    if request.method == 'POST':
        # Récupérer les données de l'utilisateur (username et password) depuis le formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authentifier l'utilisateur avec les données récupérées
        user = authenticate(request, username=username, password=password)

        # Si l'utilisateur est trouvé et authentifié, se connecter et rediriger
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next', 'offres_list')  # Récupère le paramètre 'next' ou 'offres_list' par défaut
            return redirect(next_url)
        else:
            # Si les identifiants sont incorrects, afficher un message d'erreur
            error_message = "Identifiants incorrects. Veuillez réessayer."
            return render(request, 'account/login.html', {'error_message': error_message})
    
    return render(request, 'account/login.html')

@login_required
def offres_list(request):
    offres = OffreVoyage.objects.all()
    return render(request, 'offres/offres_list.html', {'offres': offres})

def offres_detail(request, offres_id):
    offre = get_object_or_404(OffreVoyage, id=offres_id)
    return render(request, 'offres/offre_details.html', {'offre': offre})

def index(request):
    return redirect('login')
