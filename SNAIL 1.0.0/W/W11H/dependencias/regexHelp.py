import re
import os
class regexHelp:
    """
    Engine de Processamento de Linguagem Natural para Strings (Versão Inclusiva).

    Esta classe traduz comandos em texto simples para operações complexas de fatiamento 
    e Expressões Regulares em Python. Diferente do comportamento padrão do Python, 
    todos os limites superiores (B) nesta classe são INCLUSIVOS.

    COMANDOS DISPONÍVEIS:

    BUSCA E EXTRAÇÃO:
    - "line <num> from file <path>": Extrai a linha X de um arquivo no disco.
    - "line <num> from string <text>": Extrai a linha X de um bloco de texto.
    - "char <A> to char <B>": Extrai caracteres do índice A até o índice B (inclusive).
    - "char <A> to char end_of_line": Extrai do índice A até o fim da linha atual.
    - "char <A> to char beginning_of_line": Extrai do início da linha até o índice A (inclusive).
    - "<X> occurrence char <A> to <Y> occurrence char <B>": Extrai o texto entre a 
      X-ésima vez que A aparece e a Y-ésima vez que B aparece, incluindo a string B.

    TRANSFORMAÇÃO:
    - "replace <old> with <new>": Substitui todas as ocorrências de um termo por outro.
    - "remove all whitespace": Elimina espaços, tabs e quebras de linha.
    - "trim spaces": Remove espaços apenas no início e no fim do texto.
    - "convert to uppercase": Transforma todo o texto em MAIÚSCULAS.
    - "convert to lowercase": Transforma todo o texto em minúsculas.
    - "remove empty lines": Remove linhas que estejam em branco ou contenham apenas espaços.

    VERIFICAÇÃO (Retornam True/False):
    - "contains <string>?": Verifica se um termo existe no texto.
    - "is all digits?": Verifica se o texto é composto apenas por números.
    """

    @staticmethod
    def run(command, target=None):
        """
        Executa o comando solicitado.

        Args:
            command (str): O comando em linguagem natural.
            target (str, optional): O texto alvo da operação.

        Returns:
            O resultado da operação (str, bool ou None).
        """

        # --- BUSCA E EXTRAÇÃO ---
        
        # 1. Linha de ficheiro: Retorna o conteúdo da linha X (1-based index).
        m = re.match(r"line (\d+) from file (.+)", command, re.I)
        if m:
            line_idx, path = int(m.group(1)) - 1, m.group(2).strip()
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    return lines[line_idx].strip() if line_idx < len(lines) else None
            return "Erro: Ficheiro não encontrado."

        # 2. Linha de string: Divide o target por quebras de linha e retorna a linha X.
        m = re.match(r"line (\d+) from string (.+)", command, re.I)
        if m:
            idx = int(m.group(1)) - 1
            lines = m.group(2).splitlines()
            return lines[idx] if idx < len(lines) else None

        # 3. Char A até B: Inclusivo. Ex: "char 0 to char 2" em "ABC" -> "ABC"
        m = re.match(r"char (\d+) to char (\d+)", command, re.I)
        if m and target: 
            return target[int(m.group(1)):int(m.group(2)) + 1]

        # 4. Char A até fim da linha: Pega do índice A até encontrar um \n.
        m = re.match(r"char (\d+) to char end_of_line", command, re.I)
        if m and target: 
            return target[int(m.group(1)):].split('\n')[0]

        # 5. Char A até início: Pega do índice 0 até A (inclusive).
        m = re.match(r"char (\d+) to char beginning_of_line", command, re.I)
        if m and target: 
            return target[:int(m.group(1)) + 1]

        # 6. Ocorrência X até Y: Busca padrões repetidos. 
        # Inclui o padrão final (B) no resultado.
        m = re.match(r"(\d+) occurrence char (.+) to (\d+) occurrence char (.+)", command, re.I)
        if m and target:
            try:
                start = [i.end() for i in re.finditer(re.escape(m.group(2)), target)][int(m.group(1))-1]
                end = [i.end() for i in re.finditer(re.escape(m.group(4)), target)][int(m.group(3))-1]
                return target[start:end]
            except: return None

        # --- TRANSFORMAÇÃO E LIMPEZA ---

        # 7. Substituição simples de texto.
        m = re.match(r"replace (.+) with (.+)", command, re.I)
        if m and target:
            return target.replace(m.group(1), m.group(2))

        # 8. Remoção de todos os espaços em branco (inclui tabs e novas linhas).
        if "remove all whitespace" in command.lower() and target:
            return "".join(target.split())

        # 9. Trim: Remove espaços "mortos" nas extremidades.
        if "trim spaces" in command.lower() and target:
            return target.strip()

        # 10. Caixa Alta / Baixa.
        if "convert to uppercase" in command.lower() and target:
            return target.upper()
        if "convert to lowercase" in command.lower() and target:
            return target.lower()

        # 11. Remove linhas que não contêm texto útil.
        if "remove empty lines" in command.lower() and target:
            return "\n".join([line for line in target.splitlines() if line.strip()])

        # --- VERIFICAÇÃO ---

        # 12. Busca booleana: O texto contém a substring X?
        m = re.match(r"contains (.+)\?", command, re.I)
        if m and target:
            return m.group(1) in target

        # 13. Validação numérica: A string contém apenas números?
        if "is all digits?" in command.lower() and target:
            return target.isdigit()

        return "Comando não reconhecido."