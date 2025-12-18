from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from banco_Dados.bancoDados import BancoDados
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    erro = None

    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']

        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM usuario WHERE login = ?
        """, (login,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['senha_hash'], senha):
            session['user_id'] = user['id']
            session['user_login'] = user['login']
            session['user_nome'] = user['nome']
            session['user_email'] = user['email']
            session['user_tipo'] = user['tipo']
            return redirect(url_for('index'))
        else:
            erro = "Login ou senha inválidos."

    return render_template('login.html', erro=erro)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
