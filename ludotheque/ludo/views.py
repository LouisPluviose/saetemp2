from django.shortcuts import render, HttpResponseRedirect
from . forms import CategorieForm, JeuxForm, AuteursForm, JoueursForm, CommentairesForm
from . import models

def home(request):
    template = "index.html"
    return render(request, 'ludo/index.html')

def ajoutcategorie(request):
    if request.method == "POST":
        form = CategorieForm(request)
        return render(request,"ludo/ajoutcategorie.html", {"form" : form})
    else :
        form = CategorieForm()
        return render(request, "ludo/ajoutcategorie.html", {"form" : form})

def traitementcategorie(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save()
        return HttpResponseRedirect('/ludo/')
    else :
        return render(request,"ludo/ajoutcategorie.html", {"form" : cform})

def affichagecategorie(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'ludo/affichagecategorie.html',{"liste" : liste})

def affichecategorie(request, id):
    categorie = models.Categorie.objects.get(pk = id)
    return render(request,'ludo/affichecategorie.html',{"categorie":categorie})

def updatecategorie(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CategorieForm(categorie.dico_cat())
    return render(request, "ludo/updatecategorie.html", {"form":form, "id":id})

def updatetraitementcategorie(request, id):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save(commit = False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect('/ludo/affichagecategorie')
    else:
        return render(request, "ludo/ajoutcategorie.html", {"form": cform, "id":id})

def deletecategorie(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect('/ludo/affichagecategorie')



def ajoutjeux(request):
    if request.method == "POST":
        form = JeuxForm(request)
        return render(request,"ludo/ajoutjeux.html", {"form" : form})
    else :
        form = JeuxForm()
        return render(request, "ludo/ajoutjeux.html", {"form" : form})

def traitementjeux(request):
    jform = JeuxForm(request.POST)
    if jform.is_valid():
        jeux = jform.save()
        return HttpResponseRedirect('/ludo/')
    else :
        return render(request,"ludo/ajoutjeux.html", {"form" : jform})

def affichagejeux(request):
    liste2 = list(models.Jeux.objects.all())
    return render(request, 'ludo/affichagejeux.html',{"liste" : liste2})

def affichejeux(request, id):
    jeux = models.Jeux.objects.get(pk = id)
    return render(request,'ludo/affichejeux.html',{"jeux":jeux})

def updatejeux(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    form = JeuxForm(jeux.dico_jeux())
    return render(request, "ludo/updatejeux.html", {"form":form, "id":id})

def updatetraitementjeux(request, id):
    jform = JeuxForm(request.POST)
    if jform.is_valid():
        jeux = jform.save(commit = False)
        jeux.id = id
        jeux.save()
        return HttpResponseRedirect('/ludo/affichagejeux')
    else:
        return render(request, "ludo/ajoutjeux.html", {"form": jform, "id":id})

def deletejeux(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    jeux.delete()
    return HttpResponseRedirect('/ludo/affichagejeux')



def ajoutauteurs(request):
    if request.method == "POST":
        form = AuteursForm(request)
        return render(request,"ludo/ajoutauteurs.html", {"form" : form})
    else :
        form = AuteursForm()
        return render(request, "ludo/ajoutauteurs.html", {"form" : form})

def traitementauteurs(request):
    aform = AuteursForm(request.POST)
    if aform.is_valid():
        auteurs = aform.save()
        return HttpResponseRedirect('/ludo/')
    else :
        return render(request,"ludo/ajoutauteurs.html", {"form" : aform})

def affichageauteurs(request):
    liste3 = list(models.Auteurs.objects.all())
    return render(request, 'ludo/affichageauteurs.html',{"liste" : liste3})

def afficheauteurs(request, id):
    auteurs = models.Auteurs.objects.get(pk = id)
    return render(request,'ludo/afficheauteurs.html',{"auteurs":auteurs})

def updateauteurs(request, id):
    auteurs = models.Auteurs.objects.get(pk=id)
    form = AuteursForm(auteurs.dico_aut())
    return render(request, "ludo/updateauteurs.html", {"form":form, "id":id})

def updatetraitementauteurs(request, id):
    aform = AuteursForm(request.POST)
    if aform.is_valid():
        auteurs = aform.save(commit = False)
        auteurs.id = id
        auteurs.save()
        return HttpResponseRedirect('/ludo/affichageauteurs')
    else:
        return render(request, "ludo/ajoutauteurs.html", {"form": aform, "id":id})

def deleteauteurs(request, id):
    auteurs = models.Auteurs.objects.get(pk=id)
    auteurs.delete()
    return HttpResponseRedirect('/ludo/affichageauteurs')




def ajoutjoueurs(request):
    if request.method == "POST":
        form = JoueursForm(request)
        return render(request,"ludo/ajoutjoueurs.html", {"form" : form})
    else :
        form = JoueursForm()
        return render(request, "ludo/ajoutjoueurs.html", {"form" : form})

def traitementjoueurs(request):
    jform = JoueursForm(request.POST)
    if jform.is_valid():
        joueurs = jform.save()
        return HttpResponseRedirect('/ludo/')
    else :
        return render(request,"ludo/ajoutjoueurs.html", {"form" : jform})

def affichagejoueurs(request):
    liste4 = list(models.Joueurs.objects.all())
    return render(request, 'ludo/affichagejoueurs.html',{"liste" : liste4})

def affichejoueurs(request, id):
    joueurs = models.Joueurs.objects.get(pk = id)
    return render(request,'ludo/affichejoueurs.html',{"joueurs":joueurs})

def updatejoueurs(request, id):
    joueurs = models.Joueurs.objects.get(pk=id)
    form = JoueursForm(joueurs.dico_jou())
    return render(request, "ludo/updatejoueurs.html", {"form":form, "id":id})

def updatetraitementjoueurs(request, id):
    jform = JoueursForm(request.POST)
    if jform.is_valid():
        joueurs = jform.save(commit = False)
        joueurs.id = id
        joueurs.save()
        return HttpResponseRedirect('/ludo/affichagejoueurs')
    else:
        return render(request, "ludo/ajoutjoueurs.html", {"form": jform, "id":id})

def deletejoueurs(request, id):
    joueurs = models.Joueurs.objects.get(pk=id)
    joueurs.delete()
    return HttpResponseRedirect('/ludo/affichagejoueurs')



def ajoutcommentaires(request):
    if request.method == "POST":
        form = CommentairesForm(request)
        return render(request,"ludo/ajoutcommentaires.html", {"form" : form})
    else :
        form = CommentairesForm()
        return render(request, "ludo/ajoutcommentaires.html", {"form" : form})

def traitementcommentaires(request):
    cform = CommentairesForm(request.POST)
    if cform.is_valid():
        commentaires = cform.save()
        return HttpResponseRedirect('/ludo/')
    else :
        return render(request,"ludo/ajoutcommentaires.html", {"form" : cform})

def affichagecommentaires(request):
    liste5 = list(models.Commentaires.objects.all())
    return render(request, 'ludo/affichagecommentaires.html',{"liste" : liste5})

def affichecommentaires(request, id):
    commentaires = models.Commentaires.objects.get(pk = id)
    return render(request,'ludo/affichecommentaires.html',{"commentaires":commentaires})

def updatecommentaires(request, id):
    commentaires = models.Commentaires.objects.get(pk=id)
    form = JoueursForm(commentaires.dico_com())
    return render(request, "ludo/updatecommentaires.html", {"form":form, "id":id})

def updatetraitementcommentaires(request, id):
    cform = CommentairesForm(request.POST)
    if cform.is_valid():
        commentaires = cform.save(commit = False)
        commentaires.id = id
        commentaires.save()
        return HttpResponseRedirect('/ludo/affichagecommentaires')
    else:
        return render(request, "ludo/ajoutcommentaires.html", {"form": cform, "id":id})

def deletecommentaires(request, id):
    commentaires = models.Commentaires.objects.get(pk=id)
    commentaires.delete()
    return HttpResponseRedirect('/ludo/affichagecommentaires')