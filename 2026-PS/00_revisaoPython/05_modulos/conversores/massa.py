"""
Módulo de conversão de massa.
Funções para converter entre quilogramas, libras e gramas.
"""

def kg_para_libras(kg: float) -> float:
    """
    Converte quilogramas para libras.
    1 kg = 2.20462 lb
    """
    return kg * 2.20462

def kg_para_gramas(kg: float) -> float:
    """
    Converte quilogramas para gramas.
    1 kg = 1000 g
    """
    return kg * 1000

def libras_para_kg(libras: float) -> float:
    """
    Converte libras para quilogramas.
    1 lb = 0.453592 kg
    """
    return libras * 0.453592


if __name__ == "__main__":
    print("10 kg em libras:", kg_para_libras(10))
    print("10 kg em gramas:", kg_para_gramas(10))
    print("10 lb em kg:", libras_para_kg(10))
