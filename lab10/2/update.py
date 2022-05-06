import psycopg2
from config import config

def update(name, idd):
    sql = """
    update accounts 
    set username = %s
    where user_id = %s;
    """
    
    conn = None 
    rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (idd, name))
        rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
    print(f"row={rows}")
    
    
update(1, "nurbolat")
            