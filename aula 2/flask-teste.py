from flask import Flask, render_template

dicionario = {
    1: {
        "nome": "Natalia",
        "classe": "Arqueira",
        "altura": 1.70,  
        "data_nascimento": "15/04/1990",
        "imagem": "img/necromante.jpg"
    },
    2: {
        "nome": "Viktor",
        "classe": "Necromante",
        "altura": 1.85,
        "data_nascimento": "03/12/1985",
        "imagem": "img/necromante.jpg"
    },
    3: {
        "nome": "Carla",
        "classe": "Feiticeira",
        "altura": 1.62,
        "data_nascimento": "22/07/1995",
        "imagem": "img/feiticeira.jpg"
    },
    4: {
        "nome": "Gabriel",
        "classe": "Arqueiro",
        "altura": 1.75,
        "data_nascimento": "10/09/1992",
        "imagem": "img/arqueiro.jpg"
    },
    5: {
        "nome": "Ana",
        "classe": "Feiticeira",
        "altura": 1.68,
        "data_nascimento": "20/03/1988",
        "imagem": "img/feiticeira.jpg"

    },
    6: { 
        "nome": "Cicero",
        "classe": "Necromante",
        "altura": 1.80,
        "data_nascimento": "07/06/1991",
        "imagem": "img/necromante.jpg"
    },
    7:{
        "nome": "Sonia",
        "classe": "Feiticeira",
        "altura": 1.60,
        "data_nascimento": "12/11/1987",
        "imagem": "img/feiticeira.jpg"
    }
}

app = Flask(__name__)

@app.route("/")
def inicial():
    return f"{dicionario[1]}"

@app.route("/personagem")
def mostraPersongem():
    return render_template("personagem.html", **dicionario[1])

app.run(debug=True)