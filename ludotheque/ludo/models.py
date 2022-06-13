from django.db import models

class Categorie(models.Model):
    nom_cat = models.CharField(max_length=100)
    descriptif_cat = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.nom_cat}"
        return chaine

    def dico_cat(self):
        return {"nom_cat":self.nom_cat, "descriptif_cat":self.descriptif_cat}

class Jeux(models.Model):
    titre_jeux = models.CharField(max_length=100)
    annee_jeux = models.IntegerField(blank=False)
    image_jeux = models.ImageField(upload_to='images', null = True, blank = True)
    editeur_jeux = models.CharField(max_length=100)
    auteur_jeux = models.CharField(max_length=100)
    categorie_jeux = models.ForeignKey("Categorie", on_delete=models.CASCADE)

    def __str__(self):
        chaine2 = f"{self.titre_jeux}"
        return chaine2

    def dico_jeux(self):
        return {"titre_jeux": self.titre_jeux, "anne_jeux": self.annee_jeux, "image_jeux": self.image_jeux, "editeur_jeux": self.image_jeux, "auteur_jeux": self.auteur_jeux, "categorie_jeux": self.categorie_jeux}


class Auteurs(models.Model):
    nom_aut = models.CharField(max_length=100)
    prenom_aut = models.CharField(max_length=100)
    age_aut = models.IntegerField(blank=False)
    photo_aut = models.ImageField(upload_to='images', null = True, blank = True)

    def __str__(self):
        chaine3 = f"{self.nom_aut} {self.prenom_aut}"
        return chaine3

    def dico_aut(self):
        return {"nom_aut": self.nom_aut, "prenom_aut": self.prenom_aut, "age_aut": self.age_aut, "photo_aut": self.photo_aut}

class Joueurs(models.Model):
    nom_j = models.CharField(max_length=100)
    prenom_j = models.CharField(max_length=100)
    mail_j = models.EmailField(blank=True, null=True)
    mdp_j = models.CharField(max_length=100, blank=True, null=True)
    PROFESSIONNEL = 'PROFESSIONNEL'
    PARTICULIER = 'PARTICULIER'
    choix = [(PROFESSIONNEL, 'PRO'), (PARTICULIER, 'PARTICULIER')]
    type_j = models.CharField(blank=True, choices=choix, max_length=100)

    def __str__(self):
        chaine4 = f"{self.nom_j}"
        return chaine4

    def dico_jou(self):
        return {"nom_j": self.nom_j, "prenom_j": self.prenom_j, "mail_j": self.mail_j, "mdp_j": self.mdp_j, "type_j": self.type_j}

class Commentaires(models.Model):
    jeux_com = models.ForeignKey("jeux", on_delete=models.CASCADE)
    joueurs_com = models.ForeignKey("joueurs", on_delete=models.CASCADE)
    note_com = models.IntegerField(blank=False)
    commentaire_jeu = models.TextField(null=True, blank=True)
    date_com = models.DateField(blank=True, null=True)

    def __str__(self):
        chaine5 = f"{self.commentaire_jeu}"
        return chaine5

    def dico_com(self):
        return {"jeux_com": self.jeux_com, "joueurs_com": self.joueurs_com, "note_com": self.note_com, "commentaire_jeux": self.commentaire_jeu, "date_com": self.date_com}