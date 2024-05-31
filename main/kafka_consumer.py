import pandas as pd
from json import loads
import joblib
import psycopg2 as psy
import json
from confluent_kafka import Consumer, KafkaException, KafkaError

from main import kafka_consumer
from db_connection import create_table
import joblib

from kafka_conf.Kafka import kafka_consumer
from main.db_conn import create_table

if __name__ == "__main__":
    create_table_db()
    kafka_consumer()
    