from django.contrib import admin

#from .models import portfolio

from .models import Proyecto
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado') #deja como 'solo lectura' los campos para verlos en la plataforma
# Register your models here.
admin.site.register(Proyecto, ProjectAdmin)