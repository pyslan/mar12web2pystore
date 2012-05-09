# coding: utf-8

import json

@auth.requires_login()
def simples():
    nome = request.vars.nome
    if nome:
        query = Produto.name == nome
    else:
        query = Produto
    produtos = db(query).select().as_list()
    return json.dumps(produtos)

###################################################

@service.xmlrpc
def consulta(nome):
    if nome:
        query = Produto.name.like("%%%s%%" % nome)
    else:
        query = Produto
    produtos = db(query).select().as_list()
    return produtos

@service.xmlrpc
@service.soap('MySoma', returns={'result':int}, args={'x':int, 'y': int})
def soma(x, y):
    return x + y


@service.xmlrpc
@service.soap('MyMult', returns={'result':int}, args={'x':int, 'y': int})
def mult(x, y):
    return x * y


# @auth.requires_login()
def call():
    return service()
