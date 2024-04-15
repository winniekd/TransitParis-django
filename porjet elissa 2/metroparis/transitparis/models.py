from django.db import models

class transport (models.Model) :

    id = models.AutoField(primary_key = True)
    debut = models.CharField(max_length = 50)
    fin = models.CharField(max_length = 500)
    imgligne = models.CharField(max_length = 5000)
