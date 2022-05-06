import psycopg2, csv
from config import config

with open("contacts.csv", "r") as csvv:
    contacts = list(csv.reader(csvv))
    
def insert_list(l):
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
            
n = int(input())
l = []
for i in range(n):
    l1 = input().split(" ")
    l.append(l1)
    
insert_list(l)