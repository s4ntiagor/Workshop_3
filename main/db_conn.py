



def connect_to_db():
    db_conn = None
    try:
        with open('db_config.json', 'r') as config_file:
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
            "Economy_GDP_per_Capita" BOOLEAN,
            "Social_Support" BOOLEAN,
            "Health_Life_Expectancy" BOOLEAN,
            "Freedom" BOOLEAN,
            "Corruption" BOOLEAN,
            "Generosity" BOOLEAN,
            "Happiness_Score" FLOAT,
            "Predicted_Happiness_Score" FLOAT
        );
    '''
    db_connection = None
    try:
        db_connection = connect_to_db()
        db_cursor = db_connection.cursor()
        db_cursor.execute(table_creation_sql)
        db_cursor.close()
        db_connection.commit()
        print('The "happy" table has been successfully created.')
    except (Exception, psycopg2.DatabaseError) as db_error:
        print('Error while creating the table:', db_error)
    finally:
        if db_connection is not None:
            db_connection.close()
            
def insert_data(df_all):
    insert_sql = '''
        INSERT INTO happy (
            "Economy_GDP_per_Capita", 
            "Social_Support", 
            "Health_Life_Expectancy", 
            "Freedom", 
            "Corruption", 
            "Generosity", 
            "Happiness_Score", 
            "Predicted_Happiness_Score"
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    '''
    db_connection = None
    try:
        db_connection = connect_to_db()
        db_cursor = db_connection.cursor()
        db_cursor.execute(insert_sql, (
            economy_gdp_per_capita, 
            social_support, 
            health_life_expectancy, 
            freedom, 
            corruption, 
            generosity, 
            happiness_score, 
            predicted_happiness_score
        ))
        db_cursor.close()
        db_connection.commit()
        print('Data has been successfully inserted into the "happy" table.')
    except (Exception, psycopg2.DatabaseError) as db_error:
        print('Error while inserting data:', db_error)
    finally:
        if db_connection is not None:
            db_connection.close()