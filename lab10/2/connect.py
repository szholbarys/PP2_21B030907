import imp
import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select version()")
        dvv = cur.fetchone()
        print(dvv)
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()
        
connect()