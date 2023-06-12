from django.db import models

# Create your models here.

class Compound(models.Model):
    common_name = models.CharField(max_length=500, null=True, blank=True)
    formula = models.CharField(max_length=500, null=True, blank=True)
    molecular_weight = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    heating_value = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    GWP = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.common_name
    

class Composition(models.Model):
    compound = models.ForeignKey(Compound, on_delete=models.SET_NULL, null=True)
    composition = models.DecimalField(max_digits=4, decimal_places=4, null=True, blank=True)
class EmissionInput(models.Model):
    emission_factor = models.DecimalField(max_digits=4, decimal_places=4, null=True, blank=True)
    activity = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)

    class Meta:
        #Create abstract class
        abstract =  True

class FlareInput(EmissionInput):
    flare_rate = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)