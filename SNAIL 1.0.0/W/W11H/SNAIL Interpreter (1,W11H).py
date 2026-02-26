from dependencias import funcional, memória, recolha_de_lixo, atalhos, funcional_web
ficheiro = input("Qual é o ficheiro? ")
# cabeçalho = "<SNAIL 1.0.0, "
cabeçalhos = ["<SNAIL 1.0.0, not-web, ", "<SNAIL 1.0.0, web, "]
try:
    with open(ficheiro, "r", encoding="utf-8") as file:
        primeiralinha = file.readline()
        conteúdo = file.read()
        # ajuda = primeiralinha.split(",")[1]
        # ajuda2 =ajuda.replace(" ", "")
        # ajuda4 = ajuda2.replace(",", "")
        # modo = ajuda4
        # caminho_do_interprete = primeiralinha.split(str(cabeçalho + modo))[1]
        # cabeçalho_completo = cabeçalho + modo + ", " + caminho_do_interprete + ">"
        # if modo not in ["not-web", "web"]:
        #     print("Error 8: Invalid mode.")
        #     atalhos.sair(modo=0)
        # elif primeiralinha == cabeçalho_completo:
        #     pass
        # else:
        #     print("Error 1: Invalid header.")

        if primeiralinha.startswith(cabeçalhos[0]) is True:
            caminho_do_interprete = primeiralinha.strip(cabeçalhos[0])
        elif
        temporario = modo.replace(">", "")
        modo = str(temporario.strip())
        quantidade = int(len(ficheiro + modo))
        memória.mem.guardar(1, modo)
        memória.mem.guardar(2, ficheiro)
        memória.mem.guardar(5, caminho_do_interprete)
    if primeiralinha.startswith(cabeçalho) and modo == "not-web":
        funcional.código()
    elif primeiralinha.startswith(cabeçalho) and modo == "web":
        funcional_web.código()
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





