from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published','post_categories') #personaliza columnas
    ordering = ('author', 'published') #categorías ordenamiento 
    search_fields = ('title','content','author__username','categories__name') #para campo de busqueda
    date_hierarchy = 'published' #navega por fechas
    list_filter = ('author__username','categories__name') #permite agrupar por campos

    #método para mostrar "lista de categorías"
    def post_categories(self, obj):
        return ", ".join(
            [c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
