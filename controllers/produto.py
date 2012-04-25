# coding: utf-8

def exibir():
    print "_" * 15
    #idp = request.args[0].split('-')[-1]
    # db.produto[idp]
    print request.args
    print request.vars
    return request.vars.referencia


def novo():
    form = SQLFORM(Produto).process()
    return form

def alterar():
    produto = Produto[request.args(0)]
    if produto:
        form = SQLFORM(Produto, produto.id).process()
        return form
    redirect(URL('home', 'index'))

def novacategoria():
    form = SQLFORM(Categoria)
    message = "preencha o form"
    if form.process().accepted:
        message = "sucesso"
    elif form.errors:
        message = "erro"

    return DIV(H1(message),BR(),form)
