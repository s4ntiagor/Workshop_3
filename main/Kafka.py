from json import  dumps, loads
from kafka import KafkaProducer, KafkaConsumer
import joblib
import pandas as pd
import logging
from time import sleep
from main.db_conn import insert_data

joblib_file = "C:/Users/valen/OneDrive/Documentos/ETL/workshop_3/Workshop_3/Model/random_forest_model.pkl"
model = joblib.load(joblib_file)

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
        print("Received message:", df)
        try:
            df['happiness_prediction'] = model.predict(df[['economy_gdp_per_capita', 'social_support', 'health_life_expectancy', 'freedom', 'corruption', 'generosity']])
            print("Prediction added:", df)
            insert_data(df.iloc[0])
            print("Data inserted into database Postgres:\n", df)
        except Exception as e:
            print("Error processing message:", e)