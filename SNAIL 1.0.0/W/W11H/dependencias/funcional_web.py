import memória
from dependenciasWeb import verificador
def código():
    conteúdo_do_ficheiro = open(memória.mem.ler(id_escolhido=2), "r", encoding="utf-8")
    novo = str(conteúdo_do_ficheiro).replace(";", "")
    # Remover a primeira linha
    novo2 = novo.replace(memória.mem.ler(id_escolhido=8), "")
    verificador.código()