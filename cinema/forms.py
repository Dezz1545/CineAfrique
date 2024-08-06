from django import forms

class VideoUploadForm(forms.Form):
    titre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Title',
            'required': True
        })
    )
    realisateur = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Director',
            'required': True
        })
    )
    image_couverture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'id': 'sign__gallery-upload',
            'class': 'sign__file-upload',
            'accept': '.png, .jpg, .jpeg',
            'required': True
        })
    )
    video_complete = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'id': 'sign__video-upload',
            'class': 'sign__file-upload',
            'accept': 'video/mp4,video/x-m4v,video/*',
            'required': True
        })
    )
    id_eke = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'sign__input',
            'placeholder': 'ID EKE',
            'required': True
        })
    )
