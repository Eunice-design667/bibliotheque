from django.db import models

class user(models.Model):
    nom = models.CharFields(max_length=100)

    def __str__(self):
        return self.titre

class livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre
    
class emprunt(models.Model):
    livre = models.ForeignKey(livre, on_delete=models.CASCADE)
    emprunteur = models.CharField(max_length=100)
    utilsateur = models.CharField(max_length=100)
    date_emprunt = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.emprunteur} - {self.livre.titre}"