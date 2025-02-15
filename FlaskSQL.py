from flask import Flask, render_template, g, request, session, redirect, url_for
import _sqlite3 as sq
import SQLstuff as sql



app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "yummers"


bozo_checker = False


#to turn on the server run flask --app FlaskSQL run --debug
print('running FlaskSQL file')

#FLASK TESTING


#default site/route
@app.route('/')
def index(isBozo = False):
    print("Index route called")
    rec = sql.execute_query("SELECT * FROM playerDatabase", fetch = True)
    print(f"Fetched records: {rec}")

    is_authenticated = session.get('authenticated', False)
    is_admin = session.get('adminAuthenticated', False)
    
    print(str(bozo_checker))
    #checks if the website should be rendered as a regular user, ref, or admin
    return render_template('index.html', rec = rec, is_authenticated = is_authenticated, is_admin = is_admin, bozo_checker = bozo_checker)
    

# Route for login
@app.route('/login', methods=['POST'])
def login():
    print("Login route called")  # Debugging statement
    password = request.form.get('password')
    if password == "LUNA":
        session['authenticated'] = True
        return redirect(url_for('index'))
    if password == "Limax":
        session['adminAuthenticated'] = True
        return redirect(url_for('index'))
    else:
        bozo_checker = True
        return redirect(url_for('index', isBozo = True))

# Route for logout
@app.route('/logout', methods=['POST'])
def logout():
    print("Logout route called")  # Debugging statement
    session['authenticated'] = False
    session['adminAuthenticated'] = False
    return redirect(url_for('index'))

@app.route("/hello/")
def hello(name = None):
    return '<p>hewwo</p>'