# coding: utf-8

# id criado obrigatoriamente
# format
# notnull, unique, default
# compute, represent, widget, writable, readable
# Virtual, Lazy field
# validator (quantidade maxima por item)

Categoria = db.define_table("categoria",
        Field("nome", "string"),
        Field("descricao", "text"),
        Field("foto", "upload"),
        Field("%(nome)s"),
    )

Produto = db.define_table("produto",
        Field("categoria", "reference categoria"),
        Field("name"),
        Field("descricao", "text"),
        Field("peso", "double"),
        Field("preco", "decimal"),
        Field("estoque", "integer"),
        Field("foto", "upload"),
        Field("miniatura", "upload"), # T / F
        Field("destaque", "boolean", default=False),
        Field("email_enviado", "boolean", default=False),
        Field("quantidade_maxima", "integer", default=5),
        format = lambda row: "%(nome)s" % row
    )

# virtual peso total e preco total

Pedido = db.define_table("pedido",
        Field("comprador", "reference auth_user"),
        Field("itens", "integer"),
        Field("valor", "decimal"),
        Field("enviar_para", "reference enderecos")
        Field("status"),
    )

PedidoItens = db.define_table("pedido_itens",
        Field("pedido_id", "reference pedido"),
        Field("produto_id", Produto), # db.pedido
        Field("quantidade", "integer"),
        Field("preco_atual", "decimal"),
        Field("valor_total", "decimal"),
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

