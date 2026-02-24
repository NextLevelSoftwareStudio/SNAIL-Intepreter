import re, memória, atalhos
from pathlib import Path
bibliotecas = []
ficheiro = memória.mem.ler(2)
conteúdo = open(ficheiro, "r").read()
def código():
    def extrair(texto, palavra):
        padrao = rf"{re.escape(palavra)}(.*?)(?=(?://)|$)"
        resultados = re.findall(padrao, texto, re.MULTILINE)
        return [r.strip() for r in resultados]
    def extrair2(texto, palavra):
        padrao = rf"{re.escape(palavra)}(.*?)(?=(?://)|[\"#]|$)"
        resultados = re.findall(padrao, conteúdo, re.MULTILINE)
        return [r.strip() for r in resultados]
    bibliotecas_com_from = {}
    if "import " in conteúdo:
            encontrados = extrair(conteúdo, "import ")
            for linha in encontrados:
                for item in linha.split(","):
                    partes_as = item.strip().split(" as ")
                    nome_real = partes_as[0].strip()
                    alias = partes_as[1].strip() if len(partes_as) > 1 else None
                    if nome_real and nome_real not in bibliotecas_com_from:
                        bibliotecas_com_from[nome_real] = [alias]
    if "from " in conteúdo:
            encontrados = extrair(conteúdo, "from ")
            for linha in encontrados:
                if " import " in linha:
                    partes = linha.split(" import ")
                    modulo = partes[0].strip()
                    recursos_txt = partes[1].strip()
                    if modulo not in bibliotecas_com_from:
                        bibliotecas_com_from[modulo] = [None]
                    for r in recursos_txt.split(","):
                        p_as = r.strip().split(" as ")
                        recurso_real = p_as[0].strip()
                        if recurso_real not in bibliotecas_com_from[modulo]:
                            bibliotecas_com_from[modulo].append(recurso_real)
    for lib in bibliotecas:
        if lib not in bibliotecas_com_from:
            bibliotecas_com_from[lib] = []
    code = rf"{re.escape("import ")}(.*)"
    for ocorrencia in re.finditer(code, conteúdo, re.MULTILINE):
        conteudo_extraido = ocorrencia.group(1).strip()
        c = str(conteudo_extraido)
        a = Path(extrair2(texto=c, palavra="import "))
        if '"' in a or "'" in a:
            if str(a)[3] == ":" and str(a)[4] == "\\":
                pass
            else:
                print("Error 9: Invalid import statement.")
                atalhos.sair(mode=0)
        if a.exists() is False:
            oioi = str(a).replace('"', "")
            oioi2 = str(oioi).replace("'", "")
            print(f"Error 10: File {oioi2} doesn't exists.")
            atalhos.sair(0)
        elif a.exists() is True:
            pass
        else:
            print("Something went wrong.")
    code2 = rf"{re.escape("from ")}(.*)"
    for ocorrencia in re.finditer(code2, conteúdo, re.MULTILINE):
        conteudo_extraido = ocorrencia.group(1).strip()
        c = str(conteudo_extraido)
        a = Path(extrair2(texto=c, palavra="from "))
        if '"' in a or "'" in a:
            if str(a)[2] == ":" and str(a)[3] == "\\":
                pass
            else:
                print("Error 9: Invalid import statement.")
                atalhos.sair(mode=0)
        if a.exists() is False:
            oioi = str(a).replace('"', "")
            oioi2 = str(oioi).replace("'", "")
            print(f"Error 10: File {oioi2} doesn't exists.")
            atalhos.sair(0)
        elif a.exists() is True:
            pass
        else:
            print("Something went wrong.")
    memória.mem.guardar(3, str(bibliotecas_com_from))