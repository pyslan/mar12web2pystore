# coding: utf-8

# auth
# mailer
# crypto

from gluon.tools import Auth, Mail

auth = Auth(db,
            hmac_key=Auth.get_or_create_key(),
            controller="home")

mail = Mail()
mail.settings.server = "logging"
mail.settings.sender = "loja@loja.com"
mail.settings.login = "usuario:senha"

auth.settings.mailer = mail
auth.settings.formstyle = "divs"
auth.settings.extra_fields['auth_user'] = [Field("cliente_especial", "boolean", default=False),
                                           Field("bloqueado", "boolean", default=False)]

# auth.settings.login_next = URL()

auth.define_tables()

db.auth_user.first_name.label = "Seu Primeiro Nome"
db.auth_user.first_name.comment = "Coloque seu nome"

# views, ajax, css, appadmin, languages

# generic

response.generic_patterns = ['*'] if request.is_local else ["*categoria.json"] # em tempo de desenvolvimento
#response.generic_views = ["minhafuncao.json"]

# auth.user.id
response.footer_enabled = True
response.destaque_enabled = True
