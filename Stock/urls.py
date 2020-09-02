from django.contrib import admin
from django.urls import path ,re_path
from .views import *
   
urlpatterns = [
    
    
    path('list-produit/', list_produit  , name='list_produit'),
    path('produit/', produit  , name='produit'),
    re_path(r'produit/(?P<pk>[\w-]+)/modifier', modifier_produit  , name='modifier_produit'),
  
    
    path('achat/', achat  , name='achat'),
    path('list-achat/', list_achat  , name='list_achat'),
    
    
    path('vente/', vente  , name='vente'),
    path('list-vente/', list_vente  , name='list_vente'),

    path('entree/', entree  , name='entree'),
    path('sortie/', sortie  , name='sortie'),
    path('entree-sortie/', entree_sortie  , name='entree_sortie'),


]