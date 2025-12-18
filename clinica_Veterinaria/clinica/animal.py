# clinica/animal.py

from clinica.raca import Raca
from clinica.usuario import Usuario


class Animal:
    """Representa um animal (paciente) da clínica veterinária."""

    def __init__(self, nome, idade, peso, tutor: Usuario, raca: Raca):
        if not nome:
            raise ValueError("Nome do animal não pode ser vazio.")
        if tutor is None:
            raise ValueError("Animal deve ter um tutor.")
        if raca is None:
            raise ValueError("Animal deve possuir uma raça.")

        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tutor = tutor
        self.raca = raca

    def __str__(self):
        return f"{self.nome} - {self.raca} | Tutor: {self.tutor.get_nome()}"
