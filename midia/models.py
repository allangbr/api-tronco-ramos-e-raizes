from django.db import models
from model_abs import ModelAbs

from .validators import validate_file_size
# Create your models here.

class Video(ModelAbs):
    title = models.CharField(max_length=100, unique=True)
    link_video = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'


class Audio(ModelAbs):
    file = models.FileField(upload_to='audios', validators=[validate_file_size], blank=False, null=False)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Áudio'
        verbose_name_plural = 'Áudios'


class Document(models.Model):
    file = models.FileField(upload_to='documents', validators=[validate_file_size], blank=False, null=False)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'