import memória
from dependenciasWeb import verificador
ficheiro = str(memória.mem.ler(id_escolhido=2))
def código():
    with open(ficheiro, "r", encoding="utf-8") as file:
        conteúdo_do_ficheiro = file.read()
        novo = str(conteúdo_do_ficheiro).replace(";", "")
        linhas = file.readlines()
    # Arquivo sem a primeira linha
    novo2 = linhas[1:]
    verificador.código()