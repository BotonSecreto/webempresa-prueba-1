from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts}) #inyecta post en el blog
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) #evitar el error 404 por pág desconocida con "get"
    return render(request, "blog/category.html", {'category':category})