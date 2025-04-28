from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1111"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM person
    WHERE name NOT IN (SELECT link FROM viewed_links)
    """)
    pcs = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', pcs=pcs)

@app.route('/mark_viewed', methods=['POST'])
def mark_viewed():
    conn = get_db_connection()
    cur = conn.cursor()
    # Вставляємо всі name з pc у viewed_links
    cur.execute("SELECT name FROM person")
    names = cur.fetchall()
    for name in names:
        try:
            cur.execute("INSERT INTO viewed_links (link) VALUES (%s) ON CONFLICT DO NOTHING", (name[0],))
        except:
            pass  # можна логувати
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)