from django.db import models

class BamModel(models.Model):
    start = models.IntegerField()
    region = models.IntegerField()
    mutated_allele = models.CharField()
    liftover = models.BooleanField()
    public = models.BooleanField()
