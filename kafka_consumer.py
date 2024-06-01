from main.Kafka import kafka_consumer
from main.db_conn import create_table

if __name__ == "__main__":
    create_table()
    kafka_consumer()