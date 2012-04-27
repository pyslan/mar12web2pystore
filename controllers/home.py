# coding: utf-8

def index():
    # resultado = db(Produto).select()
    # produtos = resultado.find(lambda row: row.destaque == False)
    # destaques = resultado.find(lambda row: row.destaque == True)

    #otimizada
    produtos = db(Produto).select()
    destaques = produtos.exclude(lambda row: row.destaque == True)

    return dict(produtos=produtos, destaques=destaques)

# servico json e xml basico
def consulta():
    response.footer_enabled = False
    q = request.args(0)
    if q:
        dbset = db(Produto.name.like("%%%s%%" % q))
    else:
        dbset = db(Produto)

    produtos = dbset.select(Produto.id,Produto.name, Produto.categoria)
    return dict(produtos=produtos.as_list() if request.extension == 'xml' else produtos)

def consultacategoria():
    q = request.args(0)
    if q:
        dbset = db(Categoria.nome.like("%%%s%%" % q))
    else:
        dbset = db(Categoria)

    categorias = dbset.select().as_list()
    return dict(categorias=categorias)

def user():
    #  - http://.../{application}/{controller}/authentication/login
    # - http://.../{application}/{controller}/authentication/logout
    # - http://.../{application}/{controller}/authentication/register
    # - http://.../{application}/{controller}/authentication/verify_email
    # - http://.../{application}/{controller}/authentication/retrieve_username
    # - http://.../{application}/{controller}/authentication/retrieve_password
    # - http://.../{application}/{controller}/authentication/reset_password
    # - http://.../{application}/{controller}/authentication/profile
    # - http://.../{application}/{controller}/authentication/change_password
    # request /login /logout /remember_password /profile

    escondidos = ["cliente_especial", "bloqueado"]
    for campo in escondidos:
        db.auth_user[campo].writable = db.auth_user[campo].readable = False

    form = auth()
    return form

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
