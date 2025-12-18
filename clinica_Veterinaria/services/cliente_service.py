from banco_Dados.bancoDados import BancoDados


class ClienteService:

    @staticmethod
    def buscar_cliente_por_id(cliente_id: int):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT u.id, u.nome, u.email, u.login
            FROM usuario u
            WHERE u.id = ? AND u.tipo = 'Cliente'
        """, (cliente_id,))

        cliente = cursor.fetchone()
        conn.close()

        return cliente

    @staticmethod
    def listar_animais_do_cliente(cliente_id: int):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.id, a.nome, a.idade, r.nome AS raca
            FROM animal a
            JOIN raca r ON a.id_raca = r.id
            WHERE a.id_cliente = ?
        """, (cliente_id,))

        animais = cursor.fetchall()
        conn.close()

        return animais
