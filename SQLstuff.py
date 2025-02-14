from flask import Flask
import os
import _sqlite3 as sq

app = Flask(__name__)

DATABASE = 'database.db'
cnn = sq.connect(DATABASE)
print('database connected..')
cur = cnn.cursor()


def cwd():
    return f"Current working dir: {os.getcwd()}"

def pdbinit_db():
    cur.execute('''
                CREATE TABLE IF NOT EXISTS playerDatabase (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  team TEXT,
                  name TEXT,
                  number INTEGER,
                  wins INTEGER,
                  loss INTEGER
                  )''')
    print('player database initialized..')
    
def pdbadd(team, name, number, wins, loss):
    cur.execute('''
        INSERT INTO playerDatabase (team, name, number, wins, loss)
        VALUES (?, ?, ?, ?, ?)
    ''', (team, name, number, wins, loss))
    cnn.commit()
    print(f'player name: {name} inserted into player database')

def pdbdelete(name):
    cur.execute(f'''
                DELETE FROM playerDatabase WHERE name = "{name}"
                 ''')
    cnn.commit()
    print(f'player name: {name} removed from player database')

def pdbview():
    cur.execute("SELECT * FROM playerDatabase")
    print('view..')
    return cur.fetchall()
    print('view..')
    



#init_db()
# add('Limax', 'aidan', '6264540074', 45, 6)
# add('Limax', 'adam', '6969696969', 65, 4)


pdbdelete('adam')

test = pdbview()
cur.close()
print('finished..')
