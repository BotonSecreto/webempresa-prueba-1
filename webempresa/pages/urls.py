from django.urls import path
from . import views

urlpatterns = [
     #slug de mentira para pasar la info de las páginas especiales
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]