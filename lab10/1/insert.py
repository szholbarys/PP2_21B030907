import psycopg2, csv
from config import config

with open("contacts.csv", "r") as csvv:
    contacts = list(csv.reader(csvv))
    
def insert_csv(l):
    sql = """
    INSERT INTO phonebook(First_name,Last_name, Phone_number)
    VALUES(%s, %s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, l)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
insert_csv(contacts)