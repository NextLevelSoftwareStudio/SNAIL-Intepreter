from dependencias import memória, atalhos
from dependenciasWeb import verificar_codigo_complexo
import re
def código():
    conteúdo_do_ficheiro = memória.mem.ler(id_escolhido=9)
    linhas = conteúdo_do_ficheiro.splitlines()
    if len(linhas) >= 1:
        primeira_linha = linhas[0]
    match = re.search(r'language=<(.*?)>', texto)
    if match:
        language = match.group(1)
    else:
        print("Error 12: The second line ins't a valid metadata function.")
        atalhos.sair(modo=0)
    if verificar_codigo_complexo.é_variante_valida(language) is True:
        ficheiro_html = f"""<!DOCTYPE html>
<html lang="{language}">
    <head>
        <meta charset="{encoding}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
    </body>
</html>"""
    elif verificar_codigo_complexo.é_variante_valida(language) is False:
        print("Error 12: The second line ins't a valid metadata function.")
        atalhos.sair(modo=0)