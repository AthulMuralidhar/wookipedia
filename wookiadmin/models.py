from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Continent(models.Model):
    class ContinentName(models.TextChoices):
        NORTHAMERICA = "NA", _("North America")
        SOUTHAMERICA = "SA", _("South America")
        ANTARTICA = "AN", _("Antartica")
        EUROPE = "EU", _("Europe")
        ASIA = "AS", _("Asia")
        AFRICA = "AF", _("Africa")
        AUSTRALIA = "AU", _("Australia")

    name = models.CharField(
        max_length=2, choices=ContinentName.choices, default=ContinentName.EUROPE
    )
    population = models.PositiveBigIntegerField()
    area = models.PositiveBigIntegerField()

    def __str__(self):
        return self.get_name_display()

    def clean_population(self):
        passed_population = self.cleaned_data.get("population")
        print(passed_population)
        aggregated_population = aelf.country_set.all().aggregate(
            models.Sum("population")
        )
        print(aggregated_population)

        if passed_population > aggregated_population:
            raise ValidationError(
                "The passed population is greater than the sum of the popluaitons of all the counties in the continent"
            )


class Country(models.Model):
    name = models.CharField(max_length=200)
    population = models.PositiveBigIntegerField()
    area = models.PositiveBigIntegerField()

    number_of_hospitals = models.PositiveBigIntegerField()
    number_of_schools = models.PositiveBigIntegerField()

    number_of_national_parks = models.PositiveIntegerField()
    number_of_rivers = models.PositiveIntegerField()

    continent = models.ForeignKey("Continent", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)
    population = models.PositiveBigIntegerField()
    area = models.PositiveBigIntegerField()

    number_of_roads = models.PositiveBigIntegerField()
    number_of_trees = models.PositiveBigIntegerField()
    number_of_schools = models.PositiveBigIntegerField()
    number_of_shops = models.PositiveBigIntegerField()

    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
