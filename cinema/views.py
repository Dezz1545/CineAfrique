# cinema/views.py
from django.shortcuts import render, get_object_or_404, redirect
from cinema.models import Video, VideoView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

# Page D'acceuil
def index(request):
    videos = Video.objects.filter(statut='en_ligne')  # Filtrer les vidéos en ligne et prendre les 3 premières
    return render(request, 'index.html', {'videos': videos})


def video_list(request):
    videos = Video.objects.filter(statut='en_ligne') # Vous pouvez ajouter des filtres ou ordonner les vidéos ici
    return render(request, 'video-list.html', {'videos': videos})


def single_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'single-video.html', {'video': video})


@csrf_exempt
@login_required
def update_video_views(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        video_id = data.get('video_id')
        user = request.user
        
        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Video not found'}, status=404)

        # Vérifiez si l'utilisateur a déjà vu cette vidéo
        video_view, created = VideoView.objects.get_or_create(video=video, utilisateur=user)

        if created:
            video.vues += 1
            video.save()

        return JsonResponse({'status': 'success', 'message': 'View updated successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)









