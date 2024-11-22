import json
import logging
import os
from pathlib import Path

from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer, JSONDeserializer
from confluent_kafka.serialization import StringSerializer, StringDeserializer

import consumer

# TODO exactly once - paper-producer and consumer
# TODO error handling - dead letter
# TODO prepare deployment
# TODO avro/protobuf support
# TODO autoscaling - scaling with transactional api?

logging.basicConfig(level=logging.INFO)

SCHEMA_REGISTRY = os.environ.get("SCHEMA_REGISTRY", "localhost:8081")
BOOTSTRAP_SERVER = os.environ.get("BOOTSTRAP_SERVER", "localhost:9092")
INPUT_TOPIC = os.environ.get("INPUT_TOPIC", "paper-embedded")
OUTPUT_TOPIC = os.environ.get("OUTPUT_TOPIC", "paper")
BATCH_SIZE = 64
PROJECT_ROOT = Path(__file__).parent.parent.parent


def load_schema(schema_name: str) -> dict:
    schema_path = PROJECT_ROOT / "schemas" / schema_name
    try:
        with open(schema_path) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file not found at {schema_path}")


if __name__ == '__main__':
    schema_registry_conf = {'url': SCHEMA_REGISTRY}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    string_serializer = StringSerializer('utf_8')
    string_deserializer = StringDeserializer('utf_8')

    paper_schema = load_schema("paper.json")
    paper_schema_str = json.dumps(paper_schema)
    paper_json_deserializer = JSONDeserializer(paper_schema_str, schema_registry_client)

    embedded_schema = load_schema("embedded-paper.json")
    embedded_schema_str = json.dumps(paper_schema)
    embedded_json_serializer = JSONSerializer(paper_schema_str, schema_registry_client)

    consumer_config = {
        'bootstrap.servers': BOOTSTRAP_SERVER,
        'group.id': 'embeddings',
        'auto.offset.reset': 'earliest',
        'isolation.level': 'read_committed',
        'enable.auto.commit': False,
        'key.deserializer': string_deserializer,
        'value.deserializer': paper_json_deserializer
    }

    producer_config = {
        'bootstrap.servers': BOOTSTRAP_SERVER,
        'transactional.id': 'embeddings-producer-1',
        'key.serializer': string_serializer,
        'value.serializer': embedded_json_serializer
    }

    producer = Producer(producer_config)
    consumer.run_consumer(consumer_config, producer)
