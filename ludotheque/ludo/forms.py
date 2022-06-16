from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CategorieForm(ModelForm):
    class Meta :
        model = models.Categorie
        fields = ('nom_categorie', 'descriptif_categorie')
        labels = {
            'nom_categorie' : _('Nom de la catégorie'),
            'descriptif_categorie' : _('Descriptif'),
        }

class JeuxForm(ModelForm):
    class Meta :
        model = models.Jeux
        fields = ('titre_jeux', 'annee_jeux', 'image_jeux', 'editeur_jeux', 'auteur_jeux', 'categorie_jeux')
        labels = {
            'titre_jeux' : _('Titre du jeu'),
            'annee_jeux' : _('Annee du jeu'),
            'image_jeux' : _('Image du jeu'),
            'editeur_jeux' : _('Editeur du jeu'),
            'auteur_jeux' : _('Auteur du jeu'),
            'categorie_jeux' : _('Categorie du jeu'),
        }

class AuteursForm(ModelForm):
    class Meta :
        model = models.Auteurs
        fields = ('nom_auteur', 'prenom_auteur', 'age_auteur', 'photo_auteur')
        labels = {
            'nom_auteur' : _('Nom de l\'Auteur'),
            'prenom_auteur' : _('Prenom de l\'Auteur'),
            'age_auteur' : _('Age de l\'Auteur'),
            'photo_auteur' : _('Photo de l\'Auteur'),
        }

class JoueursForm(ModelForm):
    class Meta :
        model = models.Joueurs
        fields = ('nom_joueur', 'prenom_joueur', 'prenom_joueur', 'mail_joueur', 'mdp_joueur', 'type_joueur')
        labels = {
            'nom_joueur': _('Nom du Joueur'),
            'prenom_joueur': _('Prenom du Joueur'),
            'mail_joueur' : _('Mail du Joueur'),
            'mdp_joueur' : _('Mot de passe du Joueur'),
            'type_joueur' : _('Type de Joueur'),
        }

class CommentairesForm(ModelForm):
    class Meta :
        model = models.Commentaires
        fields = ('jeux_commentaire', 'joueur_commentaire', 'note_commentaire', 'commentaire_jeu', 'date_commentaire')
        labels = {
            'jeux_commentaire' : _('Jeux commenté'),
            'joueur_commentaire' : _('Joueur'),
            'note_commentaire' : _('Note du commentaire'),
            'commentaire_jeu' : _('Commentaire Jeu' ),
            'date_commentaire' : _('Date du Commentaire'),
        }