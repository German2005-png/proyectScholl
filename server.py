from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__,static_url_path='/static')
load_dotenv()

# Configuración de la conexión MySQL
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)
# print(mysql.connection.cursor())
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `usuarios`')
    data = cur.fetchall()
    print(data)  # Esto imprimirá los datos en la consola del servidor Flask
    cur.close()  # Es importante cerrar el cursor después de usarlo
    return render_template('home.html', usuarios=data)


@app.route('/login')
def vista():
    return render_template('login.html')

@app.route('/register')
def vista2():
    return render_template('register.html')

@app.route('/regis', methods=["POST"])
def registerPost2():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)', 
                    (username, email, password))
        mysql.connection.commit()
        cur.close()
    return redirect("/")



if __name__ == '__main__':
    app.run(port=3000, debug=True)  # Esto hace que los cambios se ejecuten sin necesidad de apagarlo