from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    # URLs pour l'administration
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ajouter-film/', views.ajouter_film, name='ajouter-film'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('validation-list/', views.validation_list, name='validation-list'),
    path('modifier-profil/', views.modifier_profil, name='modifier-profil'),
    path('validation-film/', views.validation_film, name='validation-film'),
    path('validation-film/valider/<int:video_id>/', views.valider_video, name='valider_video'),
    path('validation-film/refuser/<int:video_id>/', views.refuser_video, name='refuser_video'),
    path('soumettre-support/', views.soumettre_support, name='soumettre-support'),
    


    
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
