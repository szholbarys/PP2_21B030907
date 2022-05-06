import psycopg2
from config import config

def insert(l):
    sql = """
    INSERT INTO accounts(username, email) VALUES(%s, %s);
    """
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, (l))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = [
    ("dias1", "dias1@gmail.com"),
    ("dias2", "dias2@gmail.com"),
    ("dias3", "dias3@gmail.com"),
    ("dias4", "dias4@gmail.com"),
]
insert(l)
© 2022 GitHub, Inc.