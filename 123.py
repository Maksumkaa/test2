import psycopg2
link = 'olx.gmao.com'
conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='1111', port=5432)

cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS person (
#     id INT PRIMARY KEY,
#     name VARCHAR(255)
# );
# """)

cur.execute(f"""INSERT INTO person (id, name) VALUES 
(2, '{link}');
""")

# cur.execute("""SELECT * FROM person""")

print(cur.fetchone())

conn.commit()

cur.close()
conn.close()