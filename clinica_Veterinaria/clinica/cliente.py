# clinica/cliente.py

from clinica.usuario import Usuario


class Cliente(Usuario):
    """Representa o cliente (tutor dos animais)."""

    def __init__(self, nome, email, login, senha, telefone=None, endereco=None):
        super().__init__(nome, email, login, senha, tipo="Cliente")
        self.telefone = telefone
        self.endereco = endereco
        self.animais = []

    def adicionar_animal(self, animal):
        """Adiciona um animal à lista do cliente."""
        if animal is None:
            raise ValueError("Animal não pode ser vazio.")
        self.animais.append(animal)

    def listar_animais(self):
        """Retorna a lista de animais do cliente."""
        return self.animais

