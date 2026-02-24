import memória, imports_, atalhos
import re
def código():
    def extrair(texto, palavra):
        padrao = rf"{re.escape(palavra)}(.*?)(?=(?://)|$)"
        resultados = re.findall(padrao, texto, re.MULTILINE)
        return [r.strip() for r in resultados]
    modo = memória.mem.ler(1)
    ficheiro = memória.mem.ler(2)
    bibliotecas = memória.mem.ler(3)
    try:
        imports_.código()
        with open(ficheiro, 'r', encoding='utf-8') as file:
            conteúdo = file.read()
        linhas = conteúdo.splitlines()
        conteúdo_limpo = []
        for num, linha in enumerate(linhas, start=1):
            if not linha: continue
            if not linha.endswith(';'):
                print()
    except PermissionError as e:
        print(f"Error 4: Pemission error. ({e})")
        atalhos.sair(modo=0)
    except Exception as e:
        print(f"Something has gone wrong. ({e})")