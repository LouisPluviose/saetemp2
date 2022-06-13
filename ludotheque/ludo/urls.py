from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('ajoutcategorie/', views.ajoutcategorie),
    path('traitementcategorie/', views.traitementcategorie),
    path('affichagecategorie/', views.affichagecategorie),
    path('affichecategorie/<int:id>/', views.affichecategorie),
    path('updatecategorie/<int:id>/', views.updatecategorie),
    path('updatetraitementcategorie/<int:id>/', views.updatetraitementcategorie),
    path('deletecategorie/<int:id>/', views.deletecategorie),

    path('ajoutjeux/', views.ajoutjeux),
    path('traitementjeux/', views.traitementjeux),
    path('affichagejeux/', views.affichagejeux),
    path('affichejeux/<int:id>/', views.affichejeux),
    path('updatejeux/<int:id>/', views.updatejeux),
    path('updatetraitementjeux/<int:id>/', views.updatetraitementjeux),
    path('deletejeux/<int:id>/', views.deletejeux),

    path('ajoutauteurs/', views.ajoutauteurs),
    path('traitementauteurs/', views.traitementauteurs),
    path('affichageauteurs/', views.affichageauteurs),
    path('afficheauteurs/<int:id>/', views.afficheauteurs),
    path('updateauteurs/<int:id>/', views.updateauteurs),
    path('updatetraitementauteurs/<int:id>/', views.updatetraitementauteurs),
    path('deleteauteurs/<int:id>/', views.deleteauteurs),

    path('ajoutjoueurs/', views.ajoutjoueurs),
    path('traitementjoueurs/', views.traitementjoueurs),
    path('affichagejoueurs/', views.affichagejoueurs),
    path('affichejoueurs/<int:id>/', views.affichejoueurs),
    path('updatejoueurs/<int:id>/', views.updatejoueurs),
    path('updatetraitementjoueurs/<int:id>/', views.updatetraitementjoueurs),
    path('deletejoueurs/<int:id>/', views.deletejoueurs),

    path('ajoutcommentaires/', views.ajoutcommentaires),
    path('traitementcommentaires/', views.traitementcommentaires),
    path('affichagecommentaires/', views.affichagecommentaires),
    path('affichecommentaires/<int:id>/', views.affichecommentaires),
    path('updatecommentaires/<int:id>/', views.updatecommentaires),
    path('updatetraitementcommentaires/<int:id>/', views.updatetraitementcommentaires),
    path('deletecommentaires/<int:id>/', views.deletecommentaires),
]