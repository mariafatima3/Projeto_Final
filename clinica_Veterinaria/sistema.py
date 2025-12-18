from flask import Flask, redirect, url_for, session, render_template
from banco_Dados.bancoDados import BancoDados
from services.inicializacao_service import (
    criar_admin_padrao,
    criar_veterinario_padrao,
    criar_cliente_padrao,
    criar_especies_e_racas
)
import os

# Import dos blueprints
from gerenciadores.auth_controller import auth_bp
from gerenciadores.cliente_controller import cliente_bp
from gerenciadores.animal_controller import animal_bp
from gerenciadores.consulta_controller import consulta_bp
from gerenciadores.funcionario_controller import funcionario_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY", "chave_super_secreta_default")
    app.config["SESSION_COOKIE_SECURE"] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    # ---------- Inicialização do banco ----------
    try:
        BancoDados.criar_tabelas()
        criar_admin_padrao()
        criar_veterinario_padrao()
        criar_cliente_padrao()
        criar_especies_e_racas()
        print("✅ Banco e usuários padrão inicializados com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar o banco: {e}")

    # ---------- Registro de blueprints ----------
    app.register_blueprint(auth_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(animal_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(funcionario_bp)

    # ---------- Rotas ----------
    @app.route("/")
    def index():
        user_tipo = session.get("user_tipo")
        if "user_id" in session and user_tipo:
            if user_tipo == "Cliente":
                return redirect(url_for("cliente.dashboard"))
            elif user_tipo in ["Veterinario", "Funcionario Clinico", "Administrador"]:
                return redirect(url_for("funcionario.dashboard"))
        return redirect(url_for("auth.login"))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)





