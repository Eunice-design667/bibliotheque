from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
    
class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    emprunteur = models.CharField(max_length=100)
    utilsateur = models.CharField(max_length=100)
    date_emprunt = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.emprunteur} - {self.livre.titre}"