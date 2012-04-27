
MEU_MENU = []
MEU_MENU.append(dict(texto="Home", url=URL("home", "index",
                                           args=['banana', 'melancia'],
                                           vars={"nome":"Bruno", "curso":"python"},
                                           anchor="container")))
MEU_MENU.append(dict(texto="Consulta", url=URL('home','consulta')))
MEU_MENU.append(dict(texto="Consulta em json", url=URL('home','consulta.json')))
MEU_MENU.append(dict(texto="Categorias", url=URL()))
