from banco_Dados.bancoDados import BancoDados
from datetime import datetime, timedelta


class ConsultaService:

    DURACAO = timedelta(minutes=30)

    @staticmethod
    def verificar_conflito(id_veterinario: int, data_hora: datetime):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        fim = data_hora + ConsultaService.DURACAO

        cursor.execute("""
            SELECT id FROM consulta
            WHERE id_veterinario = ?
            AND status = 'Agendada'
            AND data_hora BETWEEN ? AND ?
        """, (
            id_veterinario,
            data_hora.strftime('%Y-%m-%d %H:%M:%S'),
            fim.strftime('%Y-%m-%d %H:%M:%S')
        ))

        conflito = cursor.fetchone()
        conn.close()

        return conflito is not None

    @staticmethod
    def agendar(id_animal, id_veterinario, data_hora):
        if ConsultaService.verificar_conflito(id_veterinario, data_hora):
            raise ValueError("Conflito de horário com este veterinário.")

        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO consulta (data_hora, id_animal, id_veterinario)
            VALUES (?, ?, ?)
        """, (
            data_hora.strftime('%Y-%m-%d %H:%M:%S'),
            id_animal,
            id_veterinario
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def concluir(consulta_id, diagnostico, prescricao):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE consulta
            SET status = 'Concluída', diagnostico = ?
            WHERE id = ?
        """, (diagnostico, consulta_id))

        cursor.execute("""
            INSERT INTO historico (id_consulta, data_registro, tipo, descricao, detalhes)
            VALUES (?, ?, 'Consulta', ?, ?)
        """, (
            consulta_id,
            datetime.now(),
            diagnostico,
            prescricao
        ))

        conn.commit()
        conn.close()
