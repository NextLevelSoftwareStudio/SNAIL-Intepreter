import memória
from dependenciasWeb import verificador
ficheiro = str(memória.mem.ler(id_escolhido=2))
def código():
    with open(ficheiro, "r", encoding="utf-8") as file:
        conteúdo_do_ficheiro = file.read()
        linhas = file.readlines()
        novo = str(linhas).replace(";", "")
    novo2 = novo[1:]
    memória.mem.guardar(id_escolhido=9, texto=novo2)
    verificador.código()