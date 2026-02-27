from dependencias import funcional, memória, recolha_de_lixo, atalhos, funcional_web
import re
ficheiro = input("Qual é o ficheiro? ")
# cabeçalho = "<SNAIL 1.0.0, "
cabeçalhos = ["<SNAIL 1.0.0, not-web, ", "<SNAIL 1.0.0, web, "]
try:
    with open(ficheiro, "r", encoding="utf-8") as file:
        primeiralinha = file.readline()
        conteúdo = file.read()
        linhas = file.readlines()
        # Arquivo sem a primeira linha
        arquivo_novo = linhas[1:]
        # Descobrir o modo
        code = r'^<SNAIL 1.0.0, ([^,]+)'
        resultado = re.search(code, primeiralinha)
        if resultado:
            modo = resultado.group(1)
        else:
            print("Error 1: Invalid Header.")
            atalhos.sair(0)
        # Fim de descobrir o modo.
        if primeiralinha.startswith(cabeçalhos[0]) is True:
            ajuda = primeiralinha.strip(cabeçalhos[0])
            caminho_do_interprete = str(ajuda[:-1])
            cabeçalho_completo = cabeçalhos[1] + caminho_do_interprete + ">"
            memória.mem.guardar(id_escolhido=8, texto=str(cabeçalho_completo))
        elif primeiralinha.startswith(cabeçalhos[1]) is True:
            ajuda = primeiralinha.strip(cabeçalhos[1])
            caminho_do_interprete = str(ajuda[:-1])
            cabeçalho_completo = cabeçalhos[1] + caminho_do_interprete + ">"
            memória.mem.guardar(id_escolhido=8, texto=str(cabeçalho_completo))
        if primeiralinha.startswith(cabeçalhos[0]) is False and primeiralinha.startswith(cabeçalhos[1]) is False:
            oi1 = cabeçalhos[0] + caminho_do_interprete + ">"
            oi2 = cabeçalhos[1] + caminho_do_interprete + ">"
            if oi1 or oi2 in arquivo_novo:
                for i, linha in enumerate(linhas, start=1):
                    if oi1 in linha or oi2 in linha:
                        print(f"The header is correct, but it should be on line 1, not line {i}.")
                        break
        memória.mem.guardar(1, modo)
        memória.mem.guardar(2, ficheiro)
        memória.mem.guardar(5, caminho_do_interprete)
    if primeiralinha.startswith(cabeçalhos[0] + caminho_do_interprete + ">"):
        funcional.código()
    elif primeiralinha.startswith(cabeçalhos[1] + caminho_do_interprete + ">"):
        funcional_web.código()
    elif oi1 or oi2 not in conteúdo:
        print("Error 3: The header doesn't exists.")
    elif oi1 in conteúdo and primeiralinha.startswith(oi1) is False or oi2 in conteúdo and primeiralinha.startswith(oi2) is False:
        print("Error 2: The header is in a wrong place.")
    elif primeiralinha.startswith(oi1) is False or primeiralinha.startswith(oi2) is False:
        print("Error 1: Invalid header.")
    elif conteúdo == "":
        print("Error 6: The file is empty.")
except PermissionError as e:
    print(f"Error 4: Pemission error. ({e})")
except Exception as e:
    print(f"Something has gone wrong. ({e})")
recolha_de_lixo.código()