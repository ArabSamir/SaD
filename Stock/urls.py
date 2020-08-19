from django.contrib import admin
from django.urls import path ,re_path
from .views import *
   
urlpatterns = [
    
    
    path('list-produit/', list_produit  , name='list_produit'),
    path('produit/', produit  , name='produit'),
    re_path(r'produit/(?P<pk>[\w-]+)/modifier', modifier_produit  , name='modifier_produit'),
  
    
    path('entree/', entree  , name='entree'),
    path('list-entree/', list_entree  , name='list_entree'),
    
    path('sortie/', sortie  , name='sortie'),
    path('list-sortie/', list_sortie  , name='list_sortie'),



]