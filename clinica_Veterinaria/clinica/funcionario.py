# clinica/funcionario.py

from clinica.usuario import Usuario


class Funcionario(Usuario):
    """Representa um funcionário da clínica."""

    def __init__(self, nome, email, login, senha, cargo):
        super().__init__(nome, email, login, senha, tipo="Funcionario Clinico")
        self.cargo = cargo


class Administrador(Funcionario):
    """Representa o administrador do sistema."""

    def __init__(self, nome, email, login, senha):
        super().__init__(nome, email, login, senha, cargo="Administrador")
        self.tipo = "Administrador"

    def criar_usuario(self, usuario):
        if usuario is None:
            raise ValueError("Usuário inválido.")
        return True

    def remover_usuario(self, usuario):
        if usuario is None:
            raise ValueError("Usuário inválido.")
        return True
