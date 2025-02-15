from flask import Flask, render_template, g
import os
import _sqlite3 as sq

app = Flask(__name__)

DATABASE = 'database.db'
cnn = sq.connect(DATABASE)
print('database connected..')
# cur = cnn.cursor()

# Function to execute SQL queries
def execute_query(query, args=(), fetch=False):
    print(f"Executing query: {query} with args: {args}")
    with sq.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        if fetch:
            result = cursor.fetchall()
            print(f"Query fetch result: {result}")
            return result
        conn.commit()
        print("Query committed successfully")


#FLASK TESTING
@app.route('/')
def index():
    print("Index route called")
    rec = execute_query("SELECT * FROM playerDatabase", fetch = True)
    print(f"Fetched records: {rec}")
    return render_template('index.html', rec = rec)
    

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


@app.route("/hello/")
def hello(name = None):
    return '<p>hewwo</p>'




#THIS IS ALL SQLITE FUNCTIONS
def cwd():
    return f"Current working dir: {os.getcwd()}"

def pdbinit_db():
    cur = cnn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS playerDatabase (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  team TEXT,
                  name TEXT,
                  number INTEGER,
                  wins INTEGER,
                  loss INTEGER
                  )''')
    cur.close()
    print('player database initialized..')
    
def pdbadd(team, name, number, wins, loss):
    cur = cnn.cursor()
    cur.execute('''
        INSERT INTO playerDatabase (team, name, number, wins, loss)
        VALUES (?, ?, ?, ?, ?)
    ''', (team, name, number, wins, loss))
    cnn.commit()
    cur.close()
    print(f'player name: {name} inserted into player database')

def pdbdelete(name):
    cur = cnn.cursor()
    try:
        cur.execute(f'''
                    DELETE FROM playerDatabase WHERE name = "{name}"
                    ''')
        cnn.commit()
        print(f'player name: {name} removed from player database')
    except:
        print(f'player name: {name} DNE in player database')
    cur.close()
    

def pdbview():
    cur = cnn.cursor()
    cur.execute("SELECT * FROM playerDatabase")
    print('view..')
    return cur.fetchall()
    cur.close()
    

    



#init_db()
# add('Limax', 'aidan', '123456', 45, 6)
# add('Limax', 'adam', '6969696969', 65, 4)


#pdbdelete('adam')

test = pdbview()
print(test)

print('finished..')
