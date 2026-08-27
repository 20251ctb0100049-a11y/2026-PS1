/*
 * Disciplina: Programação / Orientação a Objetos
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
            System.out.println("\n--- SISTEMA DA SECRETARIA - [SEU NOME] ---");
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
                default -> System.out.println("Opção inválida! Tente novamente.");
            }
        } while (opcao != 0);
    }

    // Método auxiliar reutilizável (Retorna o objeto ou null)
    private static Aluno buscarPorMatricula(String matricula) {
        for (Aluno a : listaAlunos) {
            if (a.getMatricula().equalsIgnoreCase(matricula)) {
                return a; // Retorna a referência exata do objeto
            }
        }
        return null;
    }

    private static void cadastrarAluno() {
        System.out.print("Matrícula: ");
        String matricula = scanner.nextLine().trim();

        // Nível A: Validação de campo vazio
        if (matricula.isEmpty()) {
            System.out.println("Erro: A matrícula não pode ser vazia.");
            return;
        }

        // Nível B: Validação de matrícula única
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

        System.out.print("Idade: ");
        int idade = Integer.parseInt(scanner.nextLine());

        listaAlunos.add(new Aluno(matricula, nome, curso, idade));
        System.out.println("Aluno cadastrado com sucesso!");
    }

    private static void listarAlunos() {
        if (listaAlunos.isEmpty()) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }
        System.out.println("\n--- LISTA DE ALUNOS ---");
        for (Aluno a : listaAlunos) {
            System.out.println(a); // Usa o toString() automaticamente
        }
    }

    private static void buscarEExibirAluno() {
        System.out.print("Digite a matrícula para busca: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Aluno não encontrado.");
        } else {
            System.out.println("Encontrado: " + a);
        }
    }

    private static void atualizarAluno() {
        System.out.print("Digite a matrícula do aluno a atualizar: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Aluno não encontrado.");
            return;
        }

        System.out.print("Novo Nome (atual: " + a.getNome() + "): ");
        String novoNome = scanner.nextLine();
        if (!novoNome.isEmpty()) {
            a.setNome(novoNome); // Altera o objeto referenciado na lista
        }

        System.out.print("Novo Curso (atual: " + a.getCurso() + "): ");
        String novoCurso = scanner.nextLine();
        if (!novoCurso.isEmpty()) {
            a.setCurso(novoCurso);
        }

        System.out.println("Dados atualizados com sucesso!");
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
        System.out.println("\n--- RELATÓRIO DA SECRETARIA ---");
        System.out.println("Total de alunos cadastrados: " + listaAlunos.size());
    }
}