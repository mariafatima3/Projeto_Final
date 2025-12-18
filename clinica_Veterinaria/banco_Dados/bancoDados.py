import sqlite3
from sqlite3 import Error
from config import DATABASE


class BancoDados:
    """Gerencia conexão e estrutura do banco de dados da Clínica Veterinária."""

    @staticmethod
    def conectar():
        try:
            conn = sqlite3.connect(DATABASE)
            conn.row_factory = sqlite3.Row
            return conn
        except Error as e:
            raise RuntimeError(f"Erro ao conectar ao banco: {e}")

    @staticmethod
    def criar_tabelas():
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        try:
            
            # USUÁRIO
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    login TEXT UNIQUE NOT NULL,
                    senha_hash TEXT NOT NULL,
                    tipo TEXT NOT NULL
                );
            """)

            
            # CLIENTE
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cliente (
                    usuario_id INTEGER PRIMARY KEY,
                    telefone TEXT,
                    endereco TEXT,
                    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
                );
            """)

            
            # VETERINÁRIO
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS veterinario (
                    usuario_id INTEGER PRIMARY KEY,
                    crmv TEXT UNIQUE NOT NULL,
                    especialidade TEXT,
                    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
                );
            """)

            
            # FUNCIONÁRIO
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS funcionario (
                    usuario_id INTEGER PRIMARY KEY,
                    cargo TEXT NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
                );
            """)

            
            # ESPÉCIE
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS especie (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT UNIQUE NOT NULL
                );
            """)

            # RAÇA
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS raca (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    especie_id INTEGER NOT NULL,
                    FOREIGN KEY (especie_id) REFERENCES especie(id) ON DELETE CASCADE
                );
            """)

           
            # ANIMAL
           
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS animal (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    peso REAL NOT NULL,
                    cliente_id INTEGER NOT NULL,
                    raca_id INTEGER NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES cliente(usuario_id),
                    FOREIGN KEY (raca_id) REFERENCES raca(id)
                );
            """)

            
            # CONSULTA
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS consulta (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_hora DATETIME NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Agendada',
                    diagnostico TEXT,
                    animal_id INTEGER NOT NULL,
                    veterinario_id INTEGER NOT NULL,
                    FOREIGN KEY (animal_id) REFERENCES animal(id),
                    FOREIGN KEY (veterinario_id) REFERENCES veterinario(usuario_id)
                );
            """)

            
            # HISTÓRICO
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS historico (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    consulta_id INTEGER NOT NULL,
                    data_registro DATETIME NOT NULL,
                    tipo TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    FOREIGN KEY (consulta_id) REFERENCES consulta(id) ON DELETE CASCADE
                );
            """)

            conn.commit()
            print("✅ Banco de dados criado com sucesso!")

        except Error as e:
            conn.rollback()
            raise RuntimeError(f"Erro ao criar tabelas: {e}")

        finally:
            conn.close()

