from dependencias import memória, atalhos
from dependenciasWeb import verificar_codigo_complexo
import re, base64, webbrowser
def código():
    conteúdo_do_ficheiro = memória.mem.ler(id_escolhido=9)
    linhas = conteúdo_do_ficheiro.splitlines()
    if len(linhas) >= 1:
        primeira_linha = linhas[0]
    hihi = "metadata("
    if primeira_linha.startswith(hihi):

        # idioma

        match1 = re.search(r'language=<(.*?)>', primeira_linha)
        if match1:
            language = match1.group(1)
        else:
            print("Error 12: The second line ins't a valid metadata function.")

        # encoding
        match2 = re.search(r'encoding=<(.*?)>', primeira_linha)
        if match2:
            encoding = match2.group(1)
        else:
            print("Error 12: The second line ins't a valid metadata function.")
            atalhos.sair(modo=0)

        # título
        match4 = re.search(r'title=<(.*?)>', primeira_linha)
        if match4:
            title = match4.group(1)
        else:
            print("Error 12: The second line ins't a valid metadata function.")
            atalhos.sair(modo=0)

        memória.mem.guardar(id_escolhido=12, texto=language)
        memória.mem.guardar(id_escolhido=11, texto=encoding)
        memória.mem.guardar(id_escolhido=10, texto=title)
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
        code = re.search(r'main start(.*?)main end', conteúdo_do_ficheiro)
        if code:
            main = code.group(1)
        else:
            print("Error 13: The main from the file is missing, or is incorrect.")
            atalhos.sair(modo=0)









        # Abrindo o .html
        html_bytes = ficheiro_html.encode('utf-8')
        html_b64 = base64.b64encode(html_bytes).decode('utf-8')
        data_uri = f"data:text/html;base64,{html_b64}"
        webbrowser.open(data_uri)
    elif primeira_linha.startswith(hihi) is False:
        print("Error 12: The second line ins't a valid metadata function.")
        atalhos.sair(modo=0)
    else:
        print("Something has gone wrong.")
        atalhos.sair(modo=0)