from fileinput import filename
from django.db import models

class Pages(models.Model):
    fileName = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return 'Naam Pagina: ' + self.fileName + '----- Omschrijving: ' + self.description
    