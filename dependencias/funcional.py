import memória, imports_
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
        
    except PermissionError as e:
        print(f"Error 4: Pemission error. ({e})")
    except Exception as e:
        print(f"Something has gone wrong. ({e})")