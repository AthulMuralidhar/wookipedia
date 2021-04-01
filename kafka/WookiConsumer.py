
from kafka import KafkaConsumer

KAFKA_PORT = 'localhost:9092'
from django.core import serializers


class CityKafkaConsumer:
    def __init__(self):
        consumer = KafkaConsumer(
           'city',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='city-group',
            bootstrap_servers=KAFKA_PORT
        )
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()


    def deserialize(self):
        for data in consumer:
            yield json_serializer.deserialize(data)

                
class CountryKafkaConsumer:
    def __init__(self):
        consumer = KafkaConsumer(
           'country',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='country-group',
            bootstrap_servers=KAFKA_PORT
        )
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()


    def deserialize(self):
        for data in consumer:
            yield json_serializer.deserialize(data)

                
class ContinentKafkaConsumer:
    def __init__(self):
        consumer = KafkaConsumer(
           'continent',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='continent-group',
            bootstrap_servers=KAFKA_PORT
        )
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()


    def deserialize(self):
        for data in consumer:
            yield json_serializer.deserialize(data)

                
        