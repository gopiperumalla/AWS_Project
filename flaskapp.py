from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash and session

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('/home/ubuntu/flaskapp3/users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

# Function to query user data from the database
def get_user_by_username(username):
    conn = sqlite3.connect('/home/ubuntu/flaskapp3/users.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to insert new user into the database
def add_user(username, password, first_name, last_name, email):
    conn = sqlite3.connect('/home/ubuntu/flaskapp3/users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)', (username, password, first_name, last_name, email))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)
        if user and user[2] == password:  # user[2] is the password from the DB
            session['username'] = username
            session['first_name'] = user[3]
            session['last_name'] = user[4]
            session['email'] = user[5]
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
        if 'username' in session:
        return render_template('display.html',
                               username=session['username'],
                               first_name=session['first_name'],
                               last_name=session['last_name'],
                               email=session['email'])
    else:
        flash('You need to log in first', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        if get_user_by_username(username):
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        else:
            add_user(username, password, first_name, last_name, email)
            session['username'] = username
            session['first_name'] = first_name
            session['last_name'] = last_name
            session['email'] = email
            flash('Registration successful! Here are your details:', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
                                                                                                                                           
