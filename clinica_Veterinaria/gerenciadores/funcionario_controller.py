from flask import Blueprint, render_template, session, redirect, url_for
from banco_Dados.bancoDados import BancoDados

funcionario_bp = Blueprint('funcionario', __name__, url_prefix='/funcionario')


@funcionario_bp.route('/dashboard')
def dashboard():
    if session.get('user_tipo') not in ['Administrador', 'Funcionario Clinico', 'Veterinario']:
        return redirect(url_for('index'))

    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, login, tipo
        FROM usuario
    """)

    usuarios = cursor.fetchall()
    conn.close()

    return render_template(
        'funcionario/dashboard.html',
        usuarios=usuarios
    )


