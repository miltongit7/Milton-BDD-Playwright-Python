import os
from dotenv import load_dotenv
import psycopg2 
from psycopg2.extras import RealDictCursor
    
load_dotenv()

class DBUtils:
    @staticmethod
    def fetch_user_credentials(query, params=None):
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, params)
        credentials = cursor.fetchall()
        cursor.close()
        connection.close()
        return credentials