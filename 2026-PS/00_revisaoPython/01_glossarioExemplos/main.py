# -*- coding: utf-8 -*-
"""
==============================================================================
ARQUIVO: main.py
DISCIPLINA: Programação de Sistemas (2026-PS)
INSTITUIÇÃO: IFPR - Centro de Referência Ponta Grossa
PROFESSOR: Profe. Berssa (Dr. João Henrique Berssanette)
==============================================================================

OBJETIVO:
    Menu Unificado (Launcher) para executar todos os laboratórios.
==============================================================================
"""

import os
import sys
import time

# Mapeamento dos arquivos
laboratorios = {
    "00": ("Fundamentos e Revisão", "00_RevisaoPython.py"),
    "01": ("Comentários e Documentação", "01_Comentarios.py"),
    "02": ("Tipos de Dados e Variáveis", "02_TiposVariaveis.py"),
    "03": ("Operadores Matemáticos e Lógicos", "03_Operadores.py"),
    "04": ("Saída de Dados (Print/Format)", "04_SaidaDados.py"),
    "05": ("Entrada de Dados (Input)", "05_EntradaDados.py"),
    "06": ("Estruturas Condicionais (If/Match)", "06_EstruturasCondicionais.py"),
    "07": ("Estruturas de Repetição (Loops)", "07_EstruturasRepeticao.py"),
    "08": ("Sub-rotinas (Funções)", "08_SubRotinas.py"),
    "09": ("Estruturas de Dados (Listas/Dicts)", "09_ListasDicionarios.py"),
    "10": ("Módulos e Bibliotecas", "10_ModulosBibliotecas.py"),
    "11": ("Manipulação de Arquivos", "11_ManipulacaoArquivos.py"),
}

def limpar_tela():
    """Limpa a tela independente do Sistema Operacional."""
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cabecalho():
    limpar_tela()
    print("=" * 80)
    print("CENTRAL DE LABORATÓRIOS".center(80))
    print("🐍 Guia de Referência Rápida Python — by Profe. Berssa".center(80))
    print("Profe. Berssa | Dr. João Henrique Berssanette".center(80))
    print("🎓 IFPR - Centro de Referência Ponta Grossa".center(80))
    print("👩‍💻 Técnico em Informática 👨‍💻".center(80))
    print("=" * 80)

def menu():
    # Pega o diretório exato onde o main.py está salvo
    diretorio_base = os.path.dirname(os.path.abspath(__file__))

    while True:
        cabecalho()
        # Mostra onde o Python está procurando os arquivos (para debug)
        # print(f"📂 Diretório Base: {diretorio_base}") 
        print("\nEscolha um laboratório para iniciar:\n")
        
        for chave, (titulo, arquivo) in laboratorios.items():
            print(f"   [{chave}] {titulo}")
            
        print("\n   [S]  Sair do Sistema")
        print("-" * 80)
        
        opcao = input("Digite o número do laboratório (ex: 06): ").strip().upper()
        
        if opcao == "S":
            print("\nEncerrando... Bons estudos! 🚀")
            break
            
        if opcao in laboratorios:
            titulo, nome_arquivo = laboratorios[opcao]
            
            # Monta o caminho completo: C:\Pasta\00_RevisaoPython.py
            caminho_completo = os.path.join(diretorio_base, nome_arquivo)
            
            if os.path.exists(caminho_completo):
                print(f"\n🚀 Iniciando: {titulo}...")
                time.sleep(1)
                
                # Executa usando o caminho completo entre aspas (para evitar erro com espaços)
                os.system(f'"{sys.executable}" "{caminho_completo}"')
                
                print("\n" + "="*80)
                input("✅ Laboratório concluído. Pressione ENTER para voltar ao menu...")
            else:
                print(f"\n❌ ERRO CRÍTICO: Arquivo não encontrado!")
                print(f"   O sistema procurou em: {caminho_completo}")
                print("   Verifique se o arquivo existe e se o nome está exato.")
                input("Pressione ENTER para continuar...")
        else:
            print("\n❌ Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada.")