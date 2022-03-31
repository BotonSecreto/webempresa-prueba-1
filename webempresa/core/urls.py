#from django.contrib import admin
from django.urls import path
#from core import views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-kk/', views.about, name="about"), #url automatizada soporta cualquier nombre
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    #path('contact/', views.contact, name="contact"),
    #path('blog/', views.blog, name="blog"),
    #path('portafolio/', views.portafolio, name="portafolio"),
    #path('admin/', admin.site.urls),
]