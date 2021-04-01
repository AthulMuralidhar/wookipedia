from django.core.management.base import BaseCommand, CommandError
from wookiadmin.models import City, Continent, Country
from kafka.WookiProducer import CityKafkaProducer, CountryKafkaProducer, ContinentKafkaProducer

class Command(BaseCommand):
    help = 'sends data from django to kafka following the producer api'

    def execute(self):
        for queryset in Continent.objects.all().iteraror():
            ContinentKafkaProducer.send_to_kafka(queryset)
        
        for queryset in Country.objects.all().iteraror():
            CountrytKafkaProducer.send_to_kafka(queryset)
        
        for queryset in City.objects.all().iteraror():
            CityKafkaProducer.send_to_kafka(queryset)
      

