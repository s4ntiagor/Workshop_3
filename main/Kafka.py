from json import  dumps, loads
from kafka import KafkaProducer, KafkaConsumer
import joblib
import pandas as pd
import logging
from time import sleep
from db_conn import insert_data

def kafka_producer(row):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    message = row.to_dict()
    producer.send('kafka-prediction', value=message)
    producer.flush()  
    print("Message sent")
    
    sleep(0.2)
    
def kafka_consumer():
    consumer = KafkaConsumer(
        'kafka-new_happy',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for message in consumer:
        df = pd.json_normalize(data=message.value)
        df['happiness_prediction'] = model.predict(df[['economy_gdp_per_capita', 'social_support', 'health_life_expectancy', 'freedom', 'corruption', 'generosity']])
        insert_data(df.iloc[0])
        print("Data inserted into database Postgres:\n", df)

