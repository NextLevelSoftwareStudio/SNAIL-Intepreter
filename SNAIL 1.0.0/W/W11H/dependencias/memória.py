import ctypes
import ctypes.util
import re
import ast
class Memory:
    def __init__(self):
        libc_name = ctypes.util.find_library('c') or ('msvcrt' if ctypes.util.os.name == 'nt' else 'libc.so.6')
        self.lib = ctypes.CDLL(libc_name)
        self.lib.malloc.restype = ctypes.c_void_p
        self.tabela_ids = {}
    def alocar(self, id_escolhido, tamanho):
        if id_escolhido in self.tabela_ids:
            self.apagar(id_escolhido)
        ptr = self.lib.malloc(tamanho + 1)
        if not ptr:
            raise MemoryError("Falha ao alocar RAM.")
        self.tabela_ids[id_escolhido] = ptr
        return id_escolhido
    def guardar(self, id_escolhido, texto):
        self.alocar(id_escolhido=id_escolhido, tamanho=len(texto))
        if id_escolhido not in self.tabela_ids:
            print(f"Erro: ID {id_escolhido} não foi alocado!")
            return
        ptr = self.tabela_ids[id_escolhido]
        dados = texto.encode('utf-8')
        ctypes.memmove(ptr, dados, len(dados))
        ctypes.memset(ptr + len(dados), 0, 1)
    def ler(self, id_escolhido):
        if id_escolhido not in self.tabela_ids:
            return f"Erro: ID {id_escolhido} vazio."
        return ctypes.string_at(self.tabela_ids[id_escolhido]).decode('utf-8')
    def apagar(self, id_escolhido):
        if id_escolhido in self.tabela_ids:
            self.lib.free(self.tabela_ids[id_escolhido])
            del self.tabela_ids[id_escolhido]
    def enviar_listas(self, id_escolhido, lista):
        separador_inicial_itens = "|"
        total = sum(str(item).count(separador_inicial_itens) for item in lista)
        separador_final_itens = separador_inicial_itens * total
        for coisa in lista:
            nada = ""
            oi = type(coisa)
            oi2 = str(oi).replace("<class '", "")
            oi = oi2
            oi2 = f"{oi[:-1]}{nada}"
            total2 = sum(str(item).count(oi2) for item in lista)
            separador_final = oi2 * total2
            nova_lista = [str(item) for item in lista]
            nova_lista2 = [separador_final + item for item in nova_lista]
            nova_lista = [item + separador_final for item in nova_lista2]
            resultado = separador_final_itens.join(nova_lista)
        self.alocar(id_escolhido=id_escolhido, tamanho=len(resultado))
        self.guardar(id_escolhido=id_escolhido, texto=resultado)
    def ler_listas(self, id_escolhido):
        raw = self.ler(id_escolhido)
        if isinstance(raw, str) and raw.startswith("Erro:"):
            return []
        if not raw:
            return []
        runs = re.findall(r'\|{1,}', raw)
        sep = max(runs, key=len) if runs else None
        tokens = None
        if sep:
            tokens = [t for t in raw.split(sep) if t != '']
        else:
            max_try = min(50, max(1, len(raw) // 2))
            candidates = {}
            for l in range(1, max_try + 1):
                for i in range(len(raw) - l + 1):
                    c = raw[i:i + l]
                    if c == '':
                        continue
                    parts = [p for p in raw.split(c) if p != '']
                    if len(parts) > 1:
                        candidates[c] = max(candidates.get(c, 0), len(parts))
                if candidates:
                    break
            if candidates:
                sep = max(candidates.keys(), key=lambda k: (len(k), candidates[k]))
                tokens = [t for t in raw.split(sep) if t != '']
            else:
                tokens = [raw]
        def smallest_period(s: str) -> str:
            if not s:
                return s
            n = len(s)
            for i in range(1, n // 2 + 1):
                if n % i == 0 and s == s[:i] * (n // i):
                    return s[:i]
            return s
        def convert_by_type_name(name: str, value: str):
            name = name.strip()
            if name in ('None', 'NoneType'):
                return None
            if name == 'int':
                try:
                    return int(value)
                except Exception:
                    return value
            if name == 'float':
                try:
                    return float(value)
                except Exception:
                    return value
            if name == 'bool':
                vl = value.strip()
                if vl in ('True', 'true', '1'):
                    return True
                if vl in ('False', 'false', '0'):
                    return False
                return value
            if name == 'str':
                return value
            if name in ('list', 'tuple', 'dict', 'set'):
                try:
                    return ast.literal_eval(value)
                except Exception:
                    return value
            try:
                return ast.literal_eval(value)
            except Exception:
                return value
        results = []
        for tok in tokens:
            tok = tok
            if not tok:
                continue
            found = False
            half = len(tok) // 2
            for k in range(half, 0, -1):
                if tok[:k] == tok[-k:]:
                    wrapper = tok[:k]
                    inner = tok[k:-k]
                    if inner == '':
                        results.append('')
                        found = True
                        break
                    type_name = smallest_period(wrapper)
                    if type_name:
                        conv = convert_by_type_name(type_name, inner)
                        results.append(conv)
                        found = True
                        break
            if not found:
                try:
                    val = ast.literal_eval(tok)
                    results.append(val)
                except Exception:
                    results.append(tok)
        return results
mem = Memory()