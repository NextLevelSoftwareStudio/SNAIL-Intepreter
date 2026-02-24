import memória
variáveis_globais = []
def código():
    conteúdo_do_ficheiro = memória.mem.ler(4)
    if "var global " in conteúdo_do_ficheiro:
        