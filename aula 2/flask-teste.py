from flask import Flask, render_template

dicionario = {
    1: {
        "nome": "Natalia",
        "classe": "Arqueira",
        "altura": 1.71,  
        "data_nascimento": "15/04/1990",
        "imagem": "../static/img/arqueiro.jpg"
    },
    2: {
        "nome": "Viktor",
        "classe": "Necromante",
        "altura": 1.85,
        "data_nascimento": "03/12/1985",
        "imagem": "../static/img/necromante.jpg"
    },
    3: {
        "nome": "Carla",
        "classe": "Feiticeira",
        "altura": 1.62,
        "data_nascimento": "22/07/1995",
        "imagem": "../static/img/feiticeira.jpg"
    },
    4: {
        "nome": "Gabriel",
        "classe": "Arqueiro",
        "altura": 1.75,
        "data_nascimento": "10/09/1992",
        "imagem": "../static/img/arqueiro.jpg"
    },
    5: {
        "nome": "Ana",
        "classe": "Feiticeira",
        "altura": 1.68,
        "data_nascimento": "20/03/1988",
        "imagem": "../static/img/feiticeira.jpg"

    },
    6: { 
        "nome": "Cicero",
        "classe": "Necromante",
        "altura": 1.81,
        "data_nascimento": "07/06/1991",
        "imagem": "../static/img/necromante.jpg"
    },
    7:{
        "nome": "Sonia",
        "classe": "Feiticeira",
        "altura": 1.63,
        "data_nascimento": "12/11/1987",
        "imagem": "../static/img/feiticeira.jpg"
    }
}
usuario = {
    1: {
        "nome": "Pedro",
        "login":"portugad",
        "email": "portugad@gmail.com",
        "senha": "hotdog123",  
        "ativo": "inativo",
        "ultimo_login": "17/08/2023"
        },
    2:{
        "nome": "Ana",
        "login": "anita123",
        "email": "ana@hotemail.com",
        "senha": "senhaSegura567",
        "ativo": "ativo",
        "ultimo_login": "22/09/2023"
    },
    3:{
        "nome": "Maria",
        "login": "mariamaria",
        "email": "maria@email.com",
        "senha": "senhaMaria789",
        "ativo": "ativo",
        "ultimo_login": "12/10/2023"
    },
    4:{
        "nome": "João",
        "login": "joao123",
        "email": "joao@email.com",
        "senha": "senha123456",
        "ativo": "ativo",
        "ultimo_login": "01/09/2023"
    },
    5:{
        "nome": "Carla",
        "login": "carla.carla",
        "email": "carla@email.com",
        "senha": "senhaCarla@2023",
        "ativo": "inativo",
        "ultimo_login": "05/08/2023"
    },
    6:{
        "nome": "Fernando",
        "login": "fernan23",
        "email": "fernando@email.com",
        "senha": "fernando456!",
        "ativo": "ativo",
        "ultimo_login": "18/09/2023"
    },
    7:{
        "nome": "Isabel",
        "login": "isabel.maria",
        "email": "isabel@email.com",
        "senha": "SenhaSegura789!",
        "ativo": "ativo",
        "ultimo_login": "27/08/2023"
    }
}
app = Flask(__name__)

@app.route("/")
def mostra_personagens():
    return render_template("personagens.html", personagens=dicionario)

@app.route("/personagem/<int:personagem_id>")
def mostraPersongem(personagem_id):
    return render_template("personagem.html", **dicionario[personagem_id])

@app.route("/usuario/<int:usuario_id>")
def mostraUsuario(usuario_id):
    return render_template("usuario.html", **usuario[usuario_id])


app.run(debug=True)