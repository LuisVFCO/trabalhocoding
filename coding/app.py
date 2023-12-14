from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    database='clinica_odontologica'
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    return render_template('index.html', pacientes=pacientes)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']
    telefone = request.form['telefone']
    cursor.execute("INSERT INTO pacientes (nome, idade, email, telefone) VALUES (%s, %s, %s, %s)", (nome, idade, email, telefone))
    db.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:paciente_id>', methods=['GET', 'POST'])
def editar(paciente_id):
    if request.method == 'GET':
        cursor.execute("SELECT * FROM pacientes WHERE id = %s", paciente_id)
        paciente = cursor.fetchone()
        return render_template('editar.html', paciente=paciente)
    else:
        nome = request.form['nome']
        idade = request.form['idade']
        email = request.form['email']
        telefone = request.form['telefone']
        cursor.execute("UPDATE pacientes SET nome=%s, idade=%s, email=%s, telefone=%s WHERE id=%s", (nome, idade, email, telefone, paciente_id))
        db.commit()
        return redirect(url_for('index'))

@app.route('/deletar/<int:paciente_id>')
def deletar(paciente_id):
    cursor.execute("DELETE FROM pacientes WHERE id = %s", paciente_id)
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
