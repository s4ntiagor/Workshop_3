import pandas as pd
from json import loads
import joblib
import psycopg2 as psy
from confluent_kafka import Consumer, KafkaException, KafkaError
from Kafka import kafka_consumer
from db_conn import create_table

if __name__ == "__main__":
    create_table()
    kafka_consumer()
