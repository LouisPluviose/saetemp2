from django.db import models

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)
    descriptif_categorie = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.nom_categorie}"
        return chaine

    def dico_cat(self):
        return {"nom_categorie":self.nom_categorie, "descriptif_categorie":self.descriptif_categorie}

class Jeux(models.Model):
    titre_jeux = models.CharField(max_length=100)
    annee_jeux = models.IntegerField(blank=False)
    image_jeux = models.ImageField(upload_to='images/', null = True, blank = True)
    editeur_jeux = models.CharField(max_length=100)
    auteur_jeux = models.ForeignKey("Auteurs", on_delete=models.CASCADE, related_name="auteur_jeux")
    categorie_jeux = models.ForeignKey("Categorie", on_delete=models.CASCADE, related_name="categorie_jeux")

    def __str__(self):
        chaine2 = f"{self.titre_jeux}"
        return chaine2

    def dico_jeux(self):
        return {"titre_jeux": self.titre_jeux, "anne_jeux": self.annee_jeux, "image_jeux": self.image_jeux, "editeur_jeux": self.image_jeux, "auteur_jeux": self.auteur_jeux, "categorie_jeux": self.categorie_jeux}


class Auteurs(models.Model):
    nom_auteur = models.CharField(max_length=100)
    prenom_auteur = models.CharField(max_length=100)
    age_auteur = models.IntegerField(blank=False)
    photo_auteur= models.ImageField(upload_to='images/', null = True, blank = True)

    def __str__(self):
        chaine3 = f"{self.nom_auteur} {self.prenom_auteur}"
        return chaine3

    def dico_aut(self):
        return {"nom_auteur": self.nom_auteur, "prenom_auteur": self.prenom_auteur, "age_auteur": self.age_auteur, "photo_auteur": self.photo_auteur}

class Joueurs(models.Model):
    nom_joueur = models.CharField(max_length=100)
    prenom_joueur = models.CharField(max_length=100)
    mail_joueur = models.EmailField(blank=True, null=True)
    mdp_joueur = models.CharField(max_length=100, blank=True, null=True)
    PROFESSIONNEL = 'PROFESSIONNEL'
    PARTICULIER = 'PARTICULIER'
    choix = [(PROFESSIONNEL, 'PRO'), (PARTICULIER, 'PARTICULIER')]
    type_joueur = models.CharField(blank=True, choices=choix, max_length=100)

    def __str__(self):
        chaine4 = f"{self.nom_joueur}"
        return chaine4

    def dico_jou(self):
        return {"nom_joueur": self.nom_joueur, "prenom_joueur": self.prenom_joueur, "mail_joueur": self.mail_joueur, "mdp_joueur": self.mdp_joueur, "type_joueur": self.type_joueur}

class Commentaires(models.Model):
    jeux_commentaire = models.ForeignKey("jeux", on_delete=models.CASCADE)
    joueur_commentaire = models.ForeignKey("joueurs", on_delete=models.CASCADE)
    note_commentaire = models.IntegerField(blank=False)
    commentaire_jeu = models.TextField(null=True, blank=True)
    date_commentaire = models.DateField(blank=True, null=True)

    def __str__(self):
        chaine5 = f"{self.commentaire_jeu}"
        return chaine5

    def dico_com(self):
        return {"jeux_commentaire": self.jeux_commentaire, "joueurs_commentaire": self.joueur_commentaire, "note_commentaire": self.note_commentaire, "commentaire_jeux": self.commentaire_jeu, "date_commentaire": self.date_commentaire}