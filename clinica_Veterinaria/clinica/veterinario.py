# clinica/veterinario.py

from clinica.usuario import Usuario


class Veterinario(Usuario):
    """Representa o veterinário da clínica."""

    def __init__(self, nome, email, login, senha, crmv, especialidade=None):
        super().__init__(nome, email, login, senha, tipo="Veterinario")
        self.crmv = crmv
        self.especialidade = especialidade

    def realizar_diagnostico(self, descricao):
        """Retorna um diagnóstico registrado pelo veterinário."""
        if not descricao:
            raise ValueError("O diagnóstico não pode estar vazio.")
        return descricao
