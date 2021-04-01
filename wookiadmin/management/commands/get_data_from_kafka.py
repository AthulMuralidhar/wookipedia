from django.core.management.base import BaseCommand, CommandError
from wookiadmin.models import City, Continent, Country
from kafka.WookiConsumer import CityKafkaConsumer, ContinentKafkaConsumer, CountryKafkaConsumer
from django.core import serializers


JSONSerializer = serializers.get_serializer("json")
json_serializer = JSONSerializer()


class Command(BaseCommand):
    help = 'gets data from django to kafka following the consumer api'

    def execute(self):
        for message in ContinentKafkaConsumer.get_consumer():
            deserialised_data = json_serializer.deserialize(message)
            if deserialised_data:
                deserialised_data.save()

        for message in ConuntryKafkaConsumer.get_consumer():
            deserialised_data = json_serializer.deserialize(message)
            if deserialised_data:
                deserialised_data.save()

        for message in CityKafkaConsumer.get_consumer():
            deserialised_data = json_serializer.deserialize(message)
            if deserialised_data:
                deserialised_data.save()
            
