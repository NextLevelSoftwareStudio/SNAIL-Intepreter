import sys, recolha_de_lixo, re
def sair(modo):
    if modo == 0:
        recolha_de_lixo.código()
        sys.exit(0)
    elif modo == 1:
        print("Something has gone wrong.")
        recolha_de_lixo.código()
        sys.exit(1)