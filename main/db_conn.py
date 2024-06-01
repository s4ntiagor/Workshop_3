import psycopg2
from psycopg2 import OperationalError
import pandas as pd
import json

def connect_to_db():
    db_conn = None
    try:
        with open('./main/db_config.json', 'r') as config_file:
            db_settings = json.load(config_file)

        db_conn = psycopg2.connect(
            host='localhost',
            user=db_settings['user'],
            password=db_settings['password'],
            dbname=db_settings['database']
        )
        print('Connection to the database was successful')
    except psycopg2.DatabaseError as db_error:
        print('Failed to connect to the database:', db_error)
    return db_conn

def create_table():
    table_creation_sql = '''
        CREATE TABLE IF NOT EXISTS happy (
            "economy_gdp_per_capita" FLOAT,
            "social_support" FLOAT,
            "health_life_expectancy" FLOAT,
            "freedom" FLOAT,
            "corruption" FLOAT,
            "generosity" FLOAT,
            "happiness_score" FLOAT,
            "predicted_happiness_score" FLOAT
        );
    '''
    db_connection = None
    try:
        db_connection = connect_to_db()
        db_cursor = db_connection.cursor()
        db_cursor.execute(table_creation_sql)
        db_connection.commit()
        db_cursor.close()
        print('The "happy" table has been successfully created.')
    except (Exception, psycopg2.DatabaseError) as db_error:
        print('Error while creating the table:', db_error)
    finally:
        if db_connection is not None:
            db_connection.close()
            
def insert_data(row):
    insert_query = """
        INSERT INTO happy (            
            economy_gdp_per_capita, 
            social_support, 
            health_life_expectancy, 
            freedom, 
            corruption, 
            generosity, 
            happiness_score, 
            predicted_happiness_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cnx = None
    try:
        cnx = create_connection()
        cur = cnx.cursor()
        values = tuple(row)
        cur.execute(insert_query, values)
        cur.close()
        cnx.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error during data insertion: %s', error)
    finally:
        if cnx is not None:
            cnx.close()
            
def get_query_db():
    conn = None
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT happiness_score, predicted_happiness_score FROM happy;")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=column_names)
        cursor.close()
        return df
    except (Exception, psycopg2.DatabaseError) as db_error:
        print('Error while querying the database:', db_error)
        return None
    finally:
        if conn is not None:
            conn.close()