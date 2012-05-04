# coding: utf-8

def exibir():
    id_produto = request.args(0) or redirect(URL('home', 'index')) # redirect
    try:
        #produto = db(Produto.id == int(id_produto)).select().first()
        produto = Produto[int(id_produto)]
    except Exception:
        produto = ['erro']

    response.destaque_enabled = False

    cores = ['amarelo', 'azul']
    #form = SQLFORM.factory(Field('quantidade'), Field('id'), Field('cor', requires=IS_IN_SET(cores)))

    return dict(produto=produto, cores=cores)

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


def adicionar_ao_carrinho():
    # try / except
    id_produto = request.vars.idproduto
    quantidade = request.vars.quantidade

    # seleciona o produto no banco, caso nao exista trata o erro
    produto = Produto[int(id_produto)]

    session.carrinho = session.carrinho or []

    item = {'id': produto.id,
            'quantidade': int(quantidade),
            'nome': produto.name,
            'miniatura': produto.miniatura,
            'slug': produto.slug(),
            'preco': produto.preco,
            'total': produto.preco * int(quantidade)}

    # verificar se o item ja existe no carrinho
    # quantidade no estoque
    session.carrinho.append(item)

    redirect(URL('produto', 'carrinho'))

def carrinho():
    return dict()

def remover_do_carrinho():
    print request.vars
    print request.args


