# clinica/consulta.py

from datetime import datetime
from clinica.animal import Animal
from clinica.veterinario import Veterinario


class Consulta:
    """Representa uma consulta veterinária."""

    STATUS_AGENDADA = "Agendada"
    STATUS_EM_ATENDIMENTO = "Em Atendimento"
    STATUS_CONCLUIDA = "Concluída"

    def __init__(self, animal: Animal, veterinario: Veterinario, data_hora: datetime):
        if animal is None:
            raise ValueError("Consulta deve possuir um animal.")
        if veterinario is None:
            raise ValueError("Consulta deve possuir um veterinário.")
        if data_hora is None:
            raise ValueError("Data e hora são obrigatórias.")

        self.animal = animal
        self.veterinario = veterinario
        self.data_hora = data_hora
        self.diagnostico = None
        self.prescricao = None
        self.status = Consulta.STATUS_AGENDADA

    def iniciar_atendimento(self):
        if self.status != Consulta.STATUS_AGENDADA:
            raise ValueError("Somente consultas agendadas podem ser iniciadas.")
        self.status = Consulta.STATUS_EM_ATENDIMENTO

    def concluir_consulta(self, diagnostico: str, prescricao: str = None):
        if not diagnostico:
            raise ValueError("Diagnóstico é obrigatório para concluir a consulta.")

        self.diagnostico = diagnostico
        self.prescricao = prescricao
        self.status = Consulta.STATUS_CONCLUIDA

    def __str__(self):
        return (
            f"Consulta | {self.animal.nome} | "
            f"{self.veterinario.get_nome()} | "
            f"{self.data_hora.strftime('%d/%m/%Y %H:%M')} | "
            f"Status: {self.status}"
        )
