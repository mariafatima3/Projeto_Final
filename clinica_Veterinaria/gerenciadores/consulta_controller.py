from flask import Blueprint, render_template, request, redirect, url_for, session
from banco_Dados.bancoDados import BancoDados
from datetime import datetime

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consulta')


@consulta_bp.route('/agenda')
def agenda_diaria():
    hoje = datetime.now().date()

    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.id, c.data_hora, c.status,
               a.nome AS animal,
               u.nome AS tutor,
               v.nome AS veterinario
        FROM consulta c
        JOIN animal a ON c.id_animal = a.id
        JOIN cliente cl ON a.id_cliente = cl.id
        JOIN usuario u ON cl.id = u.id
        JOIN veterinario v ON c.id_veterinario = v.id
        WHERE date(c.data_hora) = ?
    """, (hoje,))

    consultas = cursor.fetchall()
    conn.close()

    return render_template(
        'consulta/agenda.html',
        consultas=consultas,
        hoje=hoje
    )


@consulta_bp.route('/agendar', methods=['GET', 'POST'])
def agendar_consulta():
    if request.method == 'POST':
        id_animal = request.form['id_animal']
        id_vet = request.form['id_veterinario']
        data = request.form['data']
        hora = request.form['hora']

        data_hora = f"{data} {hora}"

        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO consulta (data_hora, id_animal, id_veterinario)
            VALUES (?, ?, ?)
        """, (data_hora, id_animal, id_vet))

        conn.commit()
        conn.close()

        return redirect(url_for('consulta.agenda_diaria'))

    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM animal")
    animais = cursor.fetchall()

    cursor.execute("""
        SELECT v.id, u.nome
        FROM veterinario v
        JOIN usuario u ON v.id = u.id
    """)
    veterinarios = cursor.fetchall()

    conn.close()

    return render_template(
        'consulta/agendar.html',
        animais=animais,
        veterinarios=veterinarios
    )
