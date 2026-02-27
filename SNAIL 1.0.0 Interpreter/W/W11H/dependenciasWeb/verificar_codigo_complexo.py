import re
from dependencias import atalhos
def é_variante_valida(string_candidata):
    s = string_candidata.lower()
    padrao_formato = re.compile(r'^([a-z0-9]{5,8}|[0-9][a-z0-9]{3})$')
    if not padrao_formato.match(s):
        return False
    codigos_idioma = [c.lower() for c in atalhos.listarISO639_1Semobsoletos().values()]
    codigos_escrita = [c.lower() for c in atalhos.listarISO15924Semobsoletos().values()]
    codigos_regiao_alfa = [c.lower() for c in atalhos.listarISO3166_1alpha_2Semobsoletos().values()]
    codigos_regiao_num = [str(c) for c in atalhos.listarUN_M49().values()]
    if s in codigos_idioma:
        return False
    if s in codigos_escrita:
        return False
    if s in codigos_regiao_alfa:
        return False
    if s in codigos_regiao_num:
        return False
    return True