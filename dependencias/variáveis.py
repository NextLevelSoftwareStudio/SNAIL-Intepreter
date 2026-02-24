import memória, re, atalhos
variáveis_globais = []
def código():
    def extrair(texto, palavra):
        padrao = rf"{re.escape(palavra)}(.*?)$"
        resultados = re.findall(padrao, texto, re.MULTILINE)
        return [r.strip() for r in resultados]
    conteúdo_do_ficheiro = memória.mem.ler(4)
    atalhos.o_que_vem_depois(texto="var global ", onde_procurar=conteúdo_do_ficheiro)