import sys
from dependencias import funcional, memória, recolha_de_lixo
ficheiro = input("Qual é o ficheiro? ")
cabeçalho = "<SNAIL 1, "
try:
    with open(ficheiro, "r", encoding="utf-8") as file:
        primeiralinha = file.readline()
        conteúdo = file.read()
        modo = primeiralinha.split(cabeçalho)[1]
        if modo not in ["not-web", "web"]:
            print("Error 8: Invalid mode.")
            recolha_de_lixo.código()
            sys.exit(0)
        elif primeiralinha == cabeçalho + modo + ">":
            pass
        else:
            print("Error 1: Invalid header.")
        temporario = modo.replace(">", "")
        modo = str(temporario.strip())
        quantidade = int(len(ficheiro + modo))
        memória.mem.guardar(1, modo)
        memória.mem.guardar(2, ficheiro)
    if primeiralinha.startswith(cabeçalho):
        funcional.código()
    elif cabeçalho not in conteúdo:
        print("Error 3: The header doesn't exists.")
    elif cabeçalho in conteúdo and primeiralinha.startswith(cabeçalho) is False:
        print("Error 2: The header is in a wrong place.")
    elif primeiralinha.startswith(cabeçalho) is False:
        print("Error 1: Invalid header.")
    elif conteúdo == "":
        print("Error 6: The file is empty.")
except PermissionError as e:
    print(f"Error 4: Pemission error. ({e})")
except Exception as e:
    print(f"Something has gone wrong. ({e})")
recolha_de_lixo.código()