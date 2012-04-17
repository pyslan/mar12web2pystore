# coding: utf-8


# action nao recebe argumento
# return serializaveis - dict, list, tuple, str, numericos
# return dict - "view" - response.render(nomearquivo, context)

import datetime

def formulario():
    return DIV(
              H1("Olá"),
              FORM(
                INPUT(_type='text', _value="Bruno"),
                BR(),
                INPUT(_type='text', _value="Bruno"),
                BR(),
                TAG.BUTTON("submit")
                )
              )

def soma(x, y):
    #print "ola estou executando!!! com %s %s " % (x, y)
    return x + y

def index():
    nome = "Bruno"
    senha = 1234
    lista = ["python", "ruby", "java"]
    return dict(soma1=soma(3, 4),
                soma2=soma(30, 45),
                usuario=nome,
                linguagens=lista,
                listapronta=UL(*[LI(item.capitalize()) for item in lista],
                               _class="lista", _style="background:red;")
                )

def outra():
    return "hello world"

def hora():
    #request, cache, response, session, DAL, Field, T, *helperhtml (DIV, FORM, INPUT), IS_NOT_EMPTY
    return str(datetime.datetime.now())


def python():
    response.view = "padrao.html"
    return {
       "titulo": "Python",
       "resultado": "windows" if "indows" in request.env.http_user_agent else "outro OS"
    }

def java():
    response.view = "padrao.html"
    return {
       "titulo": "Java",
       "resultado": DIV("Java sucks!")
    }
