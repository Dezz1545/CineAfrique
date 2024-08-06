from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cinema.forms import VideoUploadForm
from .forms import RegistrationForm, CustomAuthenticationForm
from cinema.models import Video
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.db.models import Sum



#Vue Authentification
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['mot_de_passe'])
            user.save()
            return redirect('login')  # Redirigez vers la page de connexion après l'inscription
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirigez vers l'URL de votre page d'accueil
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index') 


# Vues pour l'Administration
@login_required
def validation_film(request):
    videos = Video.objects.filter(statut__in=['en_attente', 'en_revision'])
    total_videos = videos.count()
    # Obtenez le nombre total de vues
    paginator = Paginator(videos, 10)  # 10 vidéos par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'total_videos': total_videos,
        'page_obj': page_obj
    }
    return render(request, 'validation-film.html', context)


@login_required
def validation_list(request):
    video_list = Video.objects.all()  # Récupérer tous les films de la base de données
    paginator = Paginator(video_list, 6)  # Afficher 6 films par page

    page_number = request.GET.get('page')  # Récupérer le numéro de la page à afficher
    page_obj = paginator.get_page(page_number)  # Obtenir la page demandée

    total_videos = video_list.count()  # Nombre total de vidéos
    total_views = video_list.aggregate(total_views=Sum('vues'))['total_views']  # Nombre total de vues

    return render(request, 'validation-list.html', {
        'page_obj': page_obj,
        'total_videos': total_videos,
        'total_views': total_views,
    })


def valider_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.statut = 'en_ligne'
    video.save()
    messages.success(request, f'Le film "{video.titre}" a été validé.')
    return redirect('validation-film')

def refuser_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.statut = 'refuse'
    video.save()
    messages.error(request, f'Le film "{video.titre}" a été refusé.')
    return redirect('validation-film')


# Vues pour les Producteurs
@login_required
def dashboard(request):
    user = request.user
    # Obtenez les 5 vidéos les plus récentes ajoutées par l'utilisateur connecté
    videos = Video.objects.filter(utilisateur=user).order_by('-date_add')[:5]
    # Obtenez le nombre total de vidéos ajoutées par l'utilisateur connecté
    total_videos = Video.objects.filter(utilisateur=user).count()
    # Obtenez le nombre total de vues sur les vidéos ajoutées par l'utilisateur connecté
    total_views = Video.objects.filter(utilisateur=user).aggregate(total_views=Sum('vues'))['total_views'] or 0
    return render(request, 'dashboard.html', {
        'videos': videos,
        'total_videos': total_videos,
        'total_views': total_views
    })


@login_required
def ajouter_film(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            Video.objects.create(
                utilisateur=request.user,
                titre=form.cleaned_data['titre'],
                realisateur=form.cleaned_data['realisateur'],
                image_couverture=form.cleaned_data['image_couverture'],
                video_complete=form.cleaned_data['video_complete'],
                id_eke=form.cleaned_data['id_eke'],
                statut='en_attente'
            )
            return redirect('catalogue')
    else:
        form = VideoUploadForm()
    return render(request, 'ajouter-film.html', {'form': form})


@login_required
def catalogue(request):
    user = request.user
    videos = Video.objects.filter(utilisateur=user)  # Utilisez 'utilisateur' ici
    paginator = Paginator(videos, 6)  # Afficher 6 vidéos par page

    page_number = request.GET.get('page')  # Récupérer le numéro de la page à afficher
    page_obj = paginator.get_page(page_number)  # Obtenir la page demandée

    return render(request, 'catalogue.html', {'page_obj': page_obj})


@login_required
def modifier_profil(request):
    
    datas = {
         
         
    }
    
    return render(request, 'modifier-profil.html')


#Autre Vue
def soumettre_support(request):
    
    datas = {
         
         
    }
    
    return render(request, 'soumettre-support.html')