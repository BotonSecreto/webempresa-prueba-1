from django.db import models
from ckeditor.fields import RichTextField #importar app CKeditor

class Page(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    #content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido") #Edita contenido con editor CKeditor
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']

    def __str__(self):
        return self.title