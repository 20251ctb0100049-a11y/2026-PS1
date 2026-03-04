# ==============================================================================
# NOME: Rafael Lopes
# DISCIPLINA: Programação de sistemas
# DATA: 03/03/2026
# ==============================================================================
# DESCRIÇÃO: Sistema de monitoramento de estoque para loja de informática.
# ===============================================================================

def principal():
    # Armazenamento dos produtos em uma lista de dicionários
    # Cada dicionário contém o nome do item e sua quantidade atual
    estoque = [
        {"nome": "SSD 512GB NVMe", "quantidade": 3},
        {"nome": "Memória RAM 8GB DDR4", "quantidade": 15},
        {"nome": "Gabinete ATX RGB", "quantidade": 22},
        {"nome": "Placa de Vídeo RTX 4060", "quantidade": 4},
        {"nome": "Fonte 600W 80 Plus", "quantidade": 10}
    ]

    print("-" * 60)
    print(f"{'PRODUTO':<25} | {'QTD':<5} | {'SITUAÇÃO'}")
    print("-" * 60)

    # Laço 'for' para percorrer todos os produtos da lista
    for item in estoque:
        nome = item["nome"]
        qtd = item["quantidade"]

        # Estrutura condicional if/elif/else para definir a situação
        if qtd < 5:
            situacao = "Crítico"
        elif 5 <= qtd <= 20:
            situacao = "Adequado"
        else:
            situacao = "Excesso"

        # Exibição dos resultados formatados
        print(f"{nome:<25} | {qtd:<5} | {situacao}")

    print("-" * 60)

if __name__ == "__main__":
    principal()