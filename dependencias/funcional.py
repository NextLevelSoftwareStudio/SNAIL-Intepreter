import memória, imports_, atalhos
def código():
    modo = memória.mem.ler(1)
    ficheiro = memória.mem.ler(2)
    bibliotecas = memória.mem.ler(3)
    try:
        with open(ficheiro, 'r', encoding='utf-8') as file:
            conteúdo = file.read()
        ficheiro_novo = conteúdo.replace(";", "")
        imports_.código()
    except PermissionError as e:
        print(f"Error 4: Pemission error. ({e})")
        atalhos.sair(modo=0)
    except Exception as e:
        print(f"Something has gone wrong. ({e})")