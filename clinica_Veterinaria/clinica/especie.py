# clinica/especie.py

class Especie:
    """Representa uma espécie de animal (ex: Cachorro, Gato)."""

    def __init__(self, nome):
        if not nome:
            raise ValueError("Nome da espécie não pode ser vazio.")
        self.nome = nome

    def __str__(self):
        return self.nome

