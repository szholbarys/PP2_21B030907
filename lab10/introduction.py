# psgl
# \l - list all databases
# \c - database_name - connected database
# \dt - list of all tibles
# \q- quit

import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    port = "5432" 
)