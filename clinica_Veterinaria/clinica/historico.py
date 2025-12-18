# clinica/historico.py

from datetime import datetime
from clinica.consulta import Consulta


class Historico:
    """Representa um registro no histórico médico do animal."""

    TIPO_DIAGNOSTICO = "Diagnóstico"
    TIPO_PRESCRICAO = "Prescrição"
    TIPO_OBSERVACAO = "Observação"

    def __init__(self, consulta: Consulta, tipo: str, descricao: str, detalhes: str = None):
        if consulta is None:
            raise ValueError("Histórico deve estar vinculado a uma consulta.")
        if not tipo:
            raise ValueError("Tipo do histórico é obrigatório.")
        if not descricao:
            raise ValueError("Descrição do histórico é obrigatória.")

        self.consulta = consulta
        self.tipo = tipo
        self.descricao = descricao
        self.detalhes = detalhes
        self.data_registro = datetime.now()

    def __str__(self):
        return (
            f"[{self.data_registro.strftime('%d/%m/%Y %H:%M')}] "
            f"{self.tipo}: {self.descricao}"
        )
