from flask import Flask, render_template, request, redirect, url_for, session
from model.bases import *
from model.personagem import Personagem
from model.estilos import *
from model.racas import *
from model.classes import*
from model.classes_especiais import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "chave-secreta"

estilos_map = {cls().nome.lower(): cls for cls in Estilo.__subclasses__()}
racas_map = {cls().nome.lower(): cls for cls in Raca.__subclasses__()}
classes_map = {}
for sub1 in Classe.__subclasses__():        # intermediárias
    for sub2 in sub1.__subclasses__():      # concretas
        instancia = sub2()
        classes_map[instancia.nome.lower()] = sub2

@app.route("/")
def index():
    return redirect(url_for("criar_personagem"))

@app.route("/criar", methods=["GET", "POST"])
def criar_personagem():
    valores = []
    if request.method == "POST":
        # pegar dados do formulário
        nome = request.form.get("nome")
        estilo = request.form.get("estilo")
    
        if nome and estilo:
            # salvar apenas strings na session
            session["personagem"] = {
                "nome": nome,
                "estilo": estilo
            }
            
            if estilo != "clássico":
                # instanciando estilo específico
                est = Aventureiro() if estilo == "aventureiro" else Heroico()
                valores = est.gerar_atributos()

                # salva os valores na session para usar em /escolher_atributos
                session["valores"] = valores

                return redirect(url_for("escolher_atributos"))
            return redirect(url_for("escolher_raca"))
    return render_template("criar_personagem.html", valores=valores)

@app.route("/atributos", methods=["GET", "POST"])
def escolher_atributos():
    valores = session.get("valores", [])
    dados = session.get("personagem", {})
    nome = dados.get("nome")
    estilo = dados.get("estilo")

    if request.method == "POST":
        atributos_ordem = request.form.get("atributos_ordem", "")
        if atributos_ordem:
            atributos_ordem = list(map(int, atributos_ordem.split(",")))
            # Reatribui toda a dict na session
            personagem = session.get("personagem", {})
            personagem["atributos_ordem"] = atributos_ordem
            session["personagem"] = personagem
        return redirect(url_for("escolher_raca"))

    return render_template("escolher_atributos.html", valores=valores)

@app.route("/raca", methods=["GET", "POST"])
def escolher_raca():
    if request.method == "POST":
        raca = request.form.get("raca")
        personagem = session.get("personagem", {})
        personagem["raca"] = raca
        session["personagem"] = personagem  # reatribui inteiro
        return redirect(url_for("escolher_classe"))
    return render_template("escolher_raca.html", racas=list(racas_map.keys()))

@app.route("/classe", methods=["GET", "POST"])
def escolher_classe():
    if request.method == "POST":
        classe = request.form.get("classe")
        personagem = session.get("personagem", {})
        personagem["classe"] = classe
        session["personagem"] = personagem  # reatribui inteiro
        return redirect(url_for("mostrar_personagem"))
    return render_template("escolher_classe.html", classes=list(classes_map.keys()))

@app.route("/mostrar")
def mostrar_personagem():
    dados = session.get("personagem")
    if not dados:
        return redirect(url_for("criar_personagem"))

    estilo_class = estilos_map.get(dados["estilo"], Classico)
    raca_class = racas_map.get(dados["raca"], Humano)
    classe_class = classes_map.get(dados["classe"], Guerreiro)
    p1 = Personagem(nome=dados["nome"], estilo=estilo_class(), raca=raca_class(), classe=classe_class())

    if dados["estilo"] == "classico":
        # valores gerados automaticamente
        p1.receber_valores(p1.estilo.gerar_atributos())
    else:
        # aventureiro/heroico precisa da ordem escolhida
        atributos_ordem = dados.get("atributos_ordem")

        if atributos_ordem:
            # garante que p1 recebe os valores corretos
            p1.receber_valores(atributos_ordem)
        else:
            # ainda não escolheu atributos → volta para escolher
            return redirect(url_for("escolher_atributos"))

    return render_template("mostrar_personagem.html", personagem=p1)

if __name__ == "__main__":
    app.run(debug=True)