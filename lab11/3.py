import psycopg2
from config import config

def insert_list(l):
    insert = """
    INSERT INTO phonebook(first_name, last_name, phone_number) VALUES(%s, %s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(insert, (l))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = [
    ("contac1", "surname1", "+7-777-000-15-54"),
    ("contac2", "surname2", "+7-777-359-15-54"),
    ("contac3", "surname3", "+7-777-789-15-54"),
    ("contac4", "surname4", "+7-777-741-15-54"),
]

insert_list(l)