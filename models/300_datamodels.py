# coding: utf-8

import datetime

Categoria = db.define_table("categoria",
        # Field("cod", "id")
        Field("nome", "string", notnull=True),
        Field("descricao", "text"),
        Field("foto", "upload"), # caminho
        format="- %(nome)s -",
        migrate=True,
        #primarykey=["cod"]
    )

Produto = db.define_table("produto",
        Field("categoria", "reference categoria"),
        Field("subcategorias", "list:reference categoria"),
        Field("name", notnull=True),
        Field("SKU", unique=True, required=True),
        Field("descricao", "text"),
        Field("peso", "double"), #float
        Field("pesototal", "double"), #compute
        Field("preco", "double"), # Decimal
        Field("estoque", "integer"),
        Field("foto", "upload"),
        Field("miniatura", "upload"), # thumbnail
        Field("destaque", "boolean", default=False), # T / F
        Field("email_enviado", "boolean", default=False),
        Field("quantidade_maxima", "integer", default=5),
        Field("data_cadastro", "datetime", default=datetime.datetime.now())
        #format = lambda row: "%(nome)s" % row
    )

# virtual peso total e preco total

Pedido = db.define_table("pedido",
        Field("comprador", "reference auth_user"),
        Field("itens", "integer"),
        Field("valor", "double"),
        Field("enviar_para", "reference endereco"),
        Field("statuses"),
    )

PedidoItens = db.define_table("pedido_itens",
        Field("pedido_id", "reference pedido"),
        Field("produto_id", "reference produto"), # db.pedido
        Field("quantidade", "integer"),
        Field("preco_atual", "double"),
        Field("valor_total", "double"),
    )

Endereco = db.define_table("endereco",
        Field("cliente_id", "reference auth_user"),
        Field("cep"),
        Field("pais"),
        Field("estado"),
        Field("cidade"),
        Field("logradouro"),
        Field("numero"),
        Field("complemento"),
    )

