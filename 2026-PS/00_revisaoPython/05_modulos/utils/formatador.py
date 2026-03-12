# utils/formatador.py

def linha_separadora(char="=", largura=40):
    """Retorna uma linha separadora."""
    return char * largura

def formatar_resultado(origem, valor_original, unidade_origem, valor_convertido, unidade_destino):
    """Formata a exibição de um resultado de conversão."""
    return f" {origem}: {valor_original:.2f} {unidade_origem} -> {valor_convertido:.4f} {unidade_destino}"

def cabecalho_secao(titulo):
    """Retorna um cabeçalho de seção formatado."""
    sep = linha_separadora("-", len(titulo) + 4)
    return f"\n{sep}\n  {titulo}\n{sep}"
