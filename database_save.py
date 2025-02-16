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
                id SERIAL PRIMARY KEY ,
                name VARCHAR(255),
                price FLOAT,
                low_price FLOAT,
                high_price FLOAT,
                chp FLOAT,
                date VARCHAR(225)
                );
                
                """)
    CONN.commit()
    
def addValues(m, p, lp, hp, chp_ , dte=""):
    CUR.execute(f"""
                
                INSERT INTO gold_pulse_data (name, price, low_price, high_price, chp, date)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, (m, p, lp, hp, chp_, dte))
    CONN.commit()
    

