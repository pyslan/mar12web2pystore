
class VALIDATOR(object):
    def __init__(self, error_message="error", *args, **kwargs):
        self.error_message = error_message

    def __call__(self, value):
        # (value, None) - valid
        # (value, error_message) - invalid
        return (value, None)


# custom validador

class VALIDA_SKU(object):
    def __init__(self, error_message="SKU invalido"):
        self.error_message = error_message

    def __call__(self, value):
        # comece a letra A
        # 6 digitos
        if value.startswith("A") and len(value) == 6:
            return (value, None)
        else:
            return (value, self.error_message)



# validatores

Produto.SKU.requires = VALIDA_SKU()
Produto.descricao.requires=IS_NOT_EMPTY(error_message="informe uma descricao")
Produto.peso.requires=IS_NOT_EMPTY(error_message="informe um peso")
