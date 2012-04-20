# coding: utf-8

def index():
    return dict()


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
