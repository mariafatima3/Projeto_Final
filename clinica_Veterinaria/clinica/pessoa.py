# clinica/pessoa.py

class Pessoa:
    """Classe base para qualquer pessoa do sistema."""

    def __init__(self, nome: str, email: str):
        if not nome:
            raise ValueError("Nome é obrigatório.")
        if not email:
            raise ValueError("Email é obrigatório.")

        self._id = None
        self._nome = nome
        self._email = email

    # ==========================
    # GETTERS
    # ==========================
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    # ==========================
    # SETTERS
    # ==========================
    def set_id(self, id_: int):
        self._id = id_

    def set_nome(self, nome: str):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = nome

    def set_email(self, email: str):
        if not email:
            raise ValueError("Email não pode ser vazio.")
        self._email = email

    # ==========================
    # REPRESENTAÇÃO
    # ==========================
    def __str__(self):
        return f"{self._nome} <{self._email}>"
