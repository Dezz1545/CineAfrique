from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_ligne', 'En ligne'),
        ('refuse', 'Refusé'),
        ('en_revision', 'En révision'),  
    ]
    titre = models.CharField(max_length=255)
    realisateur = models.CharField(max_length=255)
    image_couverture = models.ImageField(upload_to='couvertures/')
    video_complete = models.FileField(upload_to='videos/')
    statut = models.CharField(max_length=15, choices=STATUT_CHOICES, default='en_attente')
    id_eke = models.CharField(max_length=100, unique=True)
    vues = models.PositiveIntegerField(default=0)

    # Standards
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:  # L'objet existe déjà dans la base de données
            original = Video.objects.get(pk=self.pk)
            # Comparer les champs pour voir s'ils ont changé
            if (original.titre != self.titre or
                original.realisateur != self.realisateur or
                original.image_couverture != self.image_couverture or
                original.video_complete != self.video_complete):
                self.statut = 'en_revision'
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.titre

class VideoView(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_views')
    date_viewed = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'utilisateur')

    

