from flask import Blueprint, render_template, session, redirect, url_for
from banco_Dados.bancoDados import BancoDados

cliente_bp = Blueprint('cliente', __name__, url_prefix='/cliente')


@cliente_bp.route('/dashboard')
def dashboard():
    if session.get('user_tipo') != 'Cliente':
        return redirect(url_for('index'))

    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.id, a.nome, r.nome AS raca
        FROM animal a
        JOIN raca r ON a.id_raca = r.id
        WHERE a.id_cliente = ?
    """, (session['user_id'],))

    animais = cursor.fetchall()
    conn.close()

    return render_template(
        'cliente/dashboard.html',
        animais_do_cliente=animais
    )
