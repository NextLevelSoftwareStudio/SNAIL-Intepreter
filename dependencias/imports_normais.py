import re, memória, atalhos
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
    if "import " in conteúdo:
        encontrados = extrair(conteúdo, "import ")
        for linha_import in encontrados:
            if ", " in linha_import:
                partes = [p.strip() for p in linha_import.split(", ")]
                bibliotecas.extend(partes)
            else:
                bibliotecas.append(linha_import.strip())
    bibliotecas_com_from = {}
    if "from " in conteúdo:
        encontrados = extrair(conteúdo, "from ")
        for linha_from in encontrados:
            if " import " in linha_from:
                partes = [p.strip() for p in linha_from.split(" import ")]
                modulo = partes[0]
                recurso = partes[1]
                if modulo not in bibliotecas_com_from:
                    bibliotecas_com_from[modulo] = []
                if recurso not in bibliotecas_com_from[modulo]:
                    bibliotecas_com_from[modulo].append(recurso)
    for lib in bibliotecas:
        if lib not in bibliotecas_com_from:
            bibliotecas_com_from[lib] = []
    for i in re.findall("from ", conteúdo):
        b = i[0]
        c = str(b)
        a = extrair2(texto=c, palavra="from ")
        if '"' in a:
            if str(a)[3] == ":" and str(a)[4] == "\\":
                pass
            else:
                print("Error 9: Invalid import statement.")
                atalhos.sair(mode=0)
        if a.exists is False:
            print("")
    memória.mem.guardar(3, str(bibliotecas_com_from))

# Exemplo da lista de bibliotecas extraídas:
# {
#     'os': [],
#     'sys': [],
#     'requests': [],
#     'datetime': ['datetime'],
#     'math': ['sqrt, pi']

# }
