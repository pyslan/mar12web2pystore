# coding: utf-8

# id criado obrigatoriamente

Categoria = db.define_table("categoria",
        Field("nome", "string"),
        Field("descricao", "text"),
        Field("foto", "upload"),
    )

Produto = db.define_table("produto",
        Field("categoria", "reference categoria")
    )
