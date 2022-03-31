from django.db import models

# Create your models here.
#Cada clase representa una tabla con sus campos en la BD
class Proyecto(models.Model):
    #pass
    titulo = models.CharField(max_length=200,verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to="proyects",verbose_name="Imagen") #sube imágenes al directorio 'media/proyects'
    link = models.URLField(null=True, blank=True,verbose_name="Dirección Web") #Crea el link del modelo
    creado = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación") #captura sistema
    actualizado = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición") #captura sistema
    class Meta: #subclase con METADATOS
       verbose_name = "proyecto"
       verbose_name_plural = "proyectos"
       ordering = ["-creado"] #campo de ordenación
    def __str__(self): #método que retorna nombre de proyecto
        return self.titulo