from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # URLs pour l'accueil
    path("", views.index, name="index"),
    path("video-list/", views.video_list, name="video-list"),
    path('single-video/<int:video_id>/', views.single_video, name='single-video'),
    path('update_video_views/', views.update_video_views, name='update_video_views'),
    



    
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
