# coding: utf-8

def exibir():
    print "_" * 15
    #idp = request.args[0].split('-')[-1]
    # db.produto[idp]
    print request.args
    print request.vars
    return request.vars.referencia
