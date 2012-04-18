# coding: utf-8

from gluon.storage import Storage

response.title = "loja web2py"
response.menu = []
response.meta.description = "Loja virtual"


config = Storage(
                 db=Storage(),
                 auth=Storage(),
                 mail=Storage()
                 )

config.db.uri = "sqlite://minhaloja.sqlite"

config.db.migrate_enabled = True
config.db.migrate = True
config.db.pool_size = 1
config.db.check_reserved = ['all']

config.auth.formstyle = "divs"
