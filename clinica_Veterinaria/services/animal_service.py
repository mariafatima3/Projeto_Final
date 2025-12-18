from banco_Dados.bancoDados import BancoDados


class AnimalService:

    @staticmethod
    def cadastrar(nome, idade, peso, id_cliente, id_raca):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO animal (nome, idade, peso, id_cliente, id_raca)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, idade, peso, id_cliente, id_raca))

        conn.commit()
        conn.close()

    @staticmethod
    def buscar_por_nome(termo: str):
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
        """, (f"%{termo}%",))

        animais = cursor.fetchall()
        conn.close()

        return animais

    @staticmethod
    def buscar_por_id(animal_id: int):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.*, r.nome AS raca
            FROM animal a
            JOIN raca r ON a.id_raca = r.id
            WHERE a.id = ?
        """, (animal_id,))

        animal = cursor.fetchone()
        conn.close()

        return animal
