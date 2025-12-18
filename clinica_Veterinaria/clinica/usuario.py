from werkzeug.security import generate_password_hash, check_password_hash


class Usuario:
    """Classe base para todos os usuários do sistema."""

    def __init__(self, nome, email, login, senha, tipo):
        self.nome = nome
        self.email = email
        self.login = login
        self.senha_hash = generate_password_hash(senha)
        self.tipo = tipo

    def verificar_senha(self, senha):
        """Verifica se a senha informada está correta."""
        return check_password_hash(self.senha_hash, senha)
