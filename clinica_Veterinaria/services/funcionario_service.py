from banco_Dados.bancoDados import BancoDados


class FuncionarioService:

    @staticmethod
    def listar_usuarios():
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT nome, login, tipo
            FROM usuario
        """)

        usuarios = cursor.fetchall()
        conn.close()

        return usuarios
