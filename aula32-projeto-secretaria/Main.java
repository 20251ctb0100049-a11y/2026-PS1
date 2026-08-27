/*
 * Disciplina: Programação 
 * Nome: Rafael Lopes
 * Data: 20/08/2026
 * Projeto: Secretaria do Campus
 * Arquivo: Main.java
 */

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private static ArrayList<Aluno> listaAlunos = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int opcao = -1;

        do {
            System.out.println("\n--- SISTEMA DA SECRETARIA - Rafael Lopes ---");
            System.out.println("1. Cadastrar Aluno");
            System.out.println("2. Listar Alunos");
            System.out.println("3. Buscar por Matrícula");
            System.out.println("4. Atualizar Aluno");
            System.out.println("5. Remover Aluno");
            System.out.println("6. Relatório por Curso");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");

            try {
                opcao = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                opcao = -1;
            }

            switch (opcao) {
                case 1 -> cadastrarAluno();
                case 2 -> listarAlunos();
                case 3 -> buscarEExibirAluno();
                case 4 -> atualizarAluno();
                case 5 -> removerAluno();
                case 6 -> gerarRelatorio();
                case 0 -> System.out.println("Encerrando o sistema...");
                default -> System.out.println("Opção inválida! Vale 0, 1, 2, 3, 4, 5 ou 6.");
            }
        } while (opcao != 0);
    }

    private static Aluno buscarPorMatricula(String matricula) {
        for (Aluno a : listaAlunos) {
            if (a.getMatricula().equalsIgnoreCase(matricula)) {
                return a; 
            }
        }
        return null;
    }

    private static void cadastrarAluno() {
        System.out.print("Matrícula: ");
        String matricula = scanner.nextLine().trim();

        if (matricula.isEmpty()) {
            System.out.println("Erro: A matrícula não pode ser vazia.");
            return;
        }

        if (buscarPorMatricula(matricula) != null) {
            System.out.println("Erro: Já existe um aluno cadastrado com essa matrícula.");
            return;
        }

        System.out.print("Nome: ");
        String nome = scanner.nextLine().trim();
        if (nome.isEmpty()) {
            System.out.println("Erro: O nome não pode ser vazio.");
            return;
        }

        System.out.print("Curso: ");
        String curso = scanner.nextLine().trim();

        System.out.print("Cidade: ");
        String cidade = scanner.nextLine().trim();

        listaAlunos.add(new Aluno(matricula, nome, curso, cidade));
        System.out.println("Aluno cadastrado com sucesso!");
    }

    private static void listarAlunos() {
        if (listaAlunos.isEmpty()) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }
        System.out.println("\n--- FICHAS NO GAVETEIRO: " + listaAlunos.size() + " ---");
        for (Aluno a : listaAlunos) {
            System.out.println(a); 
        }
    }

    private static void buscarEExibirAluno() {
        System.out.print("Matricula procurada: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Aluno não encontrado.");
        } else {
            System.out.println("Achei: " + a);
        }
    }

    private static void atualizarAluno() {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Aluno não encontrado.");
            return;
        }

        System.out.print("Novo curso de " + a.getNome() + ": ");
        String novoCurso = scanner.nextLine();
        if (!novoCurso.isEmpty()) {
            a.setCurso(novoCurso);
        }

        System.out.println("Ficha atualizada: " + a);
    }

    private static void removerAluno() {
        System.out.print("Digite a matrícula do aluno a remover: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Aluno não encontrado.");
            return;
        }

        System.out.print("Tem certeza que deseja remover " + a.getNome() + "? (S/N): ");
        String confirmacao = scanner.nextLine();

        if (confirmacao.equalsIgnoreCase("S")) {
            listaAlunos.remove(a);
            System.out.println("Aluno removido com sucesso.");
        } else {
            System.out.println("Remoção cancelada.");
        }
    }

    private static void gerarRelatorio() {
        System.out.println("\n--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + listaAlunos.size());

        System.out.print("Contar alunos de qual curso? ");
        String cursoProcurado = scanner.nextLine().trim();

        int contador = 0;

        for (Aluno a : listaAlunos) {
            if (a.getCurso().equalsIgnoreCase(cursoProcurado)) {
                contador++;
            }
        }

        System.out.println("Alunos de " + cursoProcurado + ": " + contador);
    }
}