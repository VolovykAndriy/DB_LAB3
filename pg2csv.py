import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="weather_db",
    user="postgres",
    password="Rthj76bn"
)

cur = conn.cursor()

cur.execute("SELECT * FROM weather_data")

column_names = [desc[0] for desc in cur.description]

with open('MySQl/weather_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(column_names)

    for row in cur:
        writer.writerow(row)

cur.execute("SELECT * FROM sky_events")

column_names = [desc[0] for desc in cur.description]

with open('MySQl/sky_events.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(column_names)

    for row in cur:
        writer.writerow(row)


cur.close()
conn.close()
