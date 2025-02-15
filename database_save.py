import os
import psycopg2
 
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1009"
DB_HOST = "localhost"
DB_PORT = "5432"
 
CONN = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
        
CUR = CONN.cursor()
    
    
def createTable():
    CUR.execute("""
                
                CREATE TABLE IF NOT EXISTS gold_pulse_data (
                id INT PRIMARY KEY,
                name VARCHAR(255),
                price FLOAT,
                low_price FLOAT,
                high_price FLOAT,
                chp FLOAT,
                date VARCHAR(225)
                );
                
                """)
    
    CONN.commit()
    

