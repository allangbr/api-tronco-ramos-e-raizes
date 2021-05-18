from django.db import models
from django.db.models.base import Model

# Create your models here.

class Document(models.Model):
    file = models.FileField(blank=False, null=False)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'