from flask import render_template, request, jsonify
from app import app, mysql
import requests

@app.route('/')
def home():
    url = "https://api.giphy.com/v1/gifs/search?api_key=tLOJJhFuBI9x5NM8YLCD3nh7JHFYnhYu&q=trip&limit=5"
    giphy = requests.get(url)
    dataGiphy = giphy.json()
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM consulta")
    registros = cursor.fetchall()
    cursor.close()
    
    return render_template('index.html', dataGiphy=dataGiphy, registros=registros)

@app.route('/add', methods=['POST'])
def add_registro():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO consulta (nombre, email) VALUES (%s, %s)", (nombre, email))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({'message': 'Registro añadido exitosamente'}), 201
