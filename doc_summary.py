import pandas as pd
import psycopg2

df = pd.read_excel("data/subpartkb-processed.xlsx")

label_counts = df['Classification'].value_counts().astype(float)
classdict = ({"label":"REQ", "label_count":label_counts[0]},
			 {"label":"DSC", "label_count":label_counts[1]},
			 {"label":"RAE", "label_count":label_counts[2]},
			 {"label":"OSR", "label_count":label_counts[3]})

conn = psycopg2.connect(
  host="localhost",
  user="metrics_user",
  password="noprod",
  database="metrics"
)

cur = conn.cursor()
cur.executemany("""INSERT INTO class_metrics (label,label_count) VALUES (%(label)s, %(label_count)s)""", classdict)
cur.execute("""SELECT * FROM class_metrics""")

print(cur.fetchall())

conn.close()