# ========================================================
# MÓDULO DE VALIDAÇÃO DE ENTRADAS
# ========================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 - Revisão: Módulos
# Autor      : Rafael Lopes
# Data       : 12/03/2026
# ========================================================

def validar_numero(valor_str: str, minimo: float = None, maximo: float = None):
    """
    Tenta converter uma string para float.
    Se não for possível, retorna (False, mensagem_erro).
    Se for possível, verifica limites mínimo e máximo.
    """
    try:
        valor = float(valor_str)
    except ValueError:
        return False, "Entrada inválida: não é um número."

    if minimo is not None and valor < minimo:
        return False, f"Valor deve ser >= {minimo}."
    if maximo is not None and valor > maximo:
        return False, f"Valor deve ser <= {maximo}."

    return True, valor
