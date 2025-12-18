from flask import Blueprint, render_template, request, redirect, url_for, session
from banco_Dados.bancoDados import BancoDados

animal_bp = Blueprint('animal', __name__, url_prefix='/animal')


@animal_bp.route('/buscar')
def buscar_animais():
    termo = request.args.get('termo', '')
    animais = []

    if termo:
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.id, a.nome, a.idade,
                   r.nome AS raca,
                   u.nome AS tutor
            FROM animal a
            JOIN raca r ON a.id_raca = r.id
            JOIN cliente c ON a.id_cliente = c.id
            JOIN usuario u ON c.id = u.id
            WHERE a.nome LIKE ?
        """, (f'%{termo}%',))

        animais = cursor.fetchall()
        conn.close()

    return render_template(
        'animal/buscar.html',
        animais=animais,
        termo=termo
    )


@animal_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastro_animal():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        peso = request.form['peso']
        id_raca = request.form['id_raca']
        id_cliente = request.form['id_tutor']

        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO animal (nome, idade, peso, id_cliente, id_raca)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, idade, peso, id_cliente, id_raca))

        conn.commit()
        conn.close()

        return redirect(url_for('animal.buscar_animais'))

    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM raca")
    racas = cursor.fetchall()

    cursor.execute("""
        SELECT u.id, u.nome, u.login
        FROM usuario u
        WHERE u.tipo = 'Cliente'
    """)
    clientes = cursor.fetchall()

    conn.close()

    return render_template(
        'animal/cadastro.html',
        racas=racas,
        clientes=clientes
    )
