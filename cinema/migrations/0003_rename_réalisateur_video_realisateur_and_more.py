# Generated by Django 5.0.7 on 2024-08-04 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_video_utilisateur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='réalisateur',
            new_name='realisateur',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vidéo_complète',
            new_name='video_complete',
        ),
    ]
