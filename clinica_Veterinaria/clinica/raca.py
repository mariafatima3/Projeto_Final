# clinica/raca.py

from clinica.especie import Especie


class Raca:
    """Representa uma raça de animal, vinculada a uma espécie."""

    def __init__(self, nome, especie: Especie):
        if not nome:
            raise ValueError("Nome da raça não pode ser vazio.")
        if not especie:
            raise ValueError("Raça deve estar vinculada a uma espécie.")

        self.nome = nome
        self.especie = especie

    def __str__(self):
        return f"{self.nome} ({self.especie})"
