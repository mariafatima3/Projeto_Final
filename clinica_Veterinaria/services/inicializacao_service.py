from banco_Dados.bancoDados import BancoDados
from werkzeug.security import generate_password_hash

def criar_admin_padrao():
    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM usuario WHERE login='admin'")
    if not cursor.fetchone():
        senha_hash = generate_password_hash("123")
        cursor.execute("""
            INSERT INTO usuario (nome, email, login, senha_hash, tipo)
            VALUES (?, ?, ?, ?, ?)
        """, ("Administrador", "admin@clinica.com", "admin", senha_hash, "Administrador"))
        conn.commit()
        print("👑 Admin criado (login: admin / senha: 123)")

    conn.close()


def criar_veterinario_padrao():
    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM usuario WHERE login='vet'")
    if not cursor.fetchone():
        senha_hash = generate_password_hash("123")
        cursor.execute("""
            INSERT INTO usuario (nome, email, login, senha_hash, tipo)
            VALUES (?, ?, ?, ?, ?)
        """, ("Dr. Carlos", "vet@clinica.com", "vet", senha_hash, "Veterinario"))
        vet_id = cursor.lastrowid
        cursor.execute("INSERT INTO veterinario (id, crmv, especialidade) VALUES (?, ?, ?)",
                       (vet_id, "CRMV1234", "Clínico Geral"))
        conn.commit()
        print("🐾 Veterinário criado (login: vet / senha: 123)")

    conn.close()


def criar_cliente_padrao():
    conn = BancoDados.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM usuario WHERE login='cliente'")
    if not cursor.fetchone():
        senha_hash = generate_password_hash("123")
        cursor.execute("""
            INSERT INTO usuario (nome, email, login, senha_hash, tipo)
            VALUES (?, ?, ?, ?, ?)
        """, ("Maria Cliente", "cliente@clinica.com", "cliente", senha_hash, "Cliente"))
        cliente_id = cursor.lastrowid
        cursor.execute("INSERT INTO cliente (id, telefone, endereco) VALUES (?, ?, ?)",
                       (cliente_id, "11999999999", "Rua Central, 123"))
        conn.commit()
        print("👤 Cliente criado (login: cliente / senha: 123)")

    conn.close()


def criar_especies_e_racas():
    conn = BancoDados.conectar()
    cursor = conn.cursor()

    especies = ["Cão", "Gato"]
    for especie in especies:
        cursor.execute("INSERT OR IGNORE INTO especie (nome) VALUES (?)", (especie,))

    cursor.execute("SELECT id FROM especie WHERE nome='Cão'")
    id_cao = cursor.fetchone()["id"]
    cursor.execute("SELECT id FROM especie WHERE nome='Gato'")
    id_gato = cursor.fetchone()["id"]

    racas = [("Labrador", id_cao), ("Poodle", id_cao), ("Siamês", id_gato), ("Persa", id_gato)]
    for nome, id_especie in racas:
        cursor.execute("INSERT OR IGNORE INTO raca (nome, id_especie) VALUES (?, ?)", (nome, id_especie))

    conn.commit()
    conn.close()
    print("🐶🐱 Espécies e raças cadastradas")
