import psycopg2
from config import config

def table():
    commonds = (
    """
        CREATE TABLE accounts (
          user_id serial PRIMARY KEY,
          username VARCHAR (50) UNIQUE NOT NULL,
          adress VARCHAR (255) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE roles (
          role_id serial PRIMARY KEY,
          role_name VARCHAR (255) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE account_roles (
          user_id INT NOT NULL,
          role_id INT NOT NULL,
          PRIMARY KEY (user_id, role_id),
          FOREIGN KEY (role_id)
            REFERENCES roles (role_id),
          FOREIGN KEY (user_id)
            REFERENCES accounts (user_id)
          
        );
        """
    )
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commonds:
            cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()
        
table()
 