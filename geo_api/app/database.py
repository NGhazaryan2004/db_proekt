import psycopg2

conn = psycopg2.connect(
    dbname="geography_db",
    user="geo_user",
    password="geo_pass",
    host="localhost"
)
