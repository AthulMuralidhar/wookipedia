from kafka import KafkaProducer


KAFKA_PORT = "localhost:9092"

from django.core import serializers

JSONSerializer = serializers.get_serializer("json")


class CityKafkaProducer:
    def __init__(self):
        producer = KafkaProducer(bootstrap_servers=KAFKA_PORT)

    def send_to_kafka(self, queryset):
        producer.send("city", value=json_serializer.serialize(query))


class CountryKafkaProducer:
    def __init__(self):
        producer = KafkaProducer(bootstrap_servers=KAFKA_PORT)

    def send_to_kafka(self, queryset):
        producer.send("country", value=json_serializer.serialize(query))


class ContinentKafkaProducer:
    def __init__(self):
        producer = KafkaProducer(bootstrap_servers=KAFKA_PORT)

    def send_to_kafka(self, queryset):
        producer.send("continent", value=json_serializer.serialize(query))
