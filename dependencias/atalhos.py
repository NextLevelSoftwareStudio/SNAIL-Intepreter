import sys, recolha_de_lixo, re
def sair(modo):
    if modo == 0:
        recolha_de_lixo.código()
        sys.exit(0)
    elif modo == 1:
        print("Something has gone wrong.")
        recolha_de_lixo.código()
        sys.exit(1)
def o_que_vem_depois(texto, onde_procurar):
    for match in re.finditer(texto, onde_procurar):
        return match.group(1)