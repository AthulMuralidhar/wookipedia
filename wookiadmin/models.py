from django.db import models
from django.utils.translation import gettext_lazy as _


class Continent(models.Model):
    class ContinentName(models.TextChoice):
        NORTHAMERICA = 'NA', _('North America')
        SOUTHAMERICA = 'SA', _('South America')
        ANTARTICA = 'AN', _('Antartica')
        EUROPE = 'EU', _('Europe')
        ASIA = 'AS', _('Asia')
        AFRICA = 'AF', _('Africa') 
        AUSTRALIA = 'AU', _('Australia')
    
    name = models.Charfield(max_length=2, choices=ContinentName.choices, default=ContinentName.EUROPE)
    population = models.PositiveBigIntegerField()
    area = models.PositiveBigIntegerField()

class Country(models.Model):
    name = models.Charfield(max_length=200)
    population = models.PositiveBigIntegerField()
    area = models.PositiveBigIntegerField()

    number_of_hospitals = models.PositiveBigIntegerField()
    number_of_schools = models.PositiveBigIntegerField()

    number_of_national_parks = models.PositiveIntegerField()
    number_of_rivers = models.PositiveIntegerField() 

    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)


class City(models.Model):
    name = models.Charfield(max_length=200)
    population = models.PositiveBigIntegerField()
    area = models.PositiveBigIntegerField()

    number_of_roads = models.PositiveBigIntegerField()
    number_of_trees = models.PositiveBigIntegerField()
    number_of_schools = models.PositiveBigIntegerField()
    number_of_shops = models.PositiveBigIntegerField()

    country = models.ForeignKey('Country', on_delete=models.CASCADE)