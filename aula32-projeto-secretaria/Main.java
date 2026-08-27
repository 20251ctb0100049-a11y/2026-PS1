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
            System.out.println("\n==========================================");
            System.out.println("   SECRETARIA DO CAMPUS - por Rafael Lopes");
            System.out.println("==========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matricula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[7] Buscar por nome");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");

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
                case 7 -> buscarPorNomeExibir();
                case 0 -> System.out.println("Secretaria fechada. Ate a proxima!");
                default -> System.out.println("Opcao invalida! Vale 0, 1, 2, 3, 4, 5, 6 ou 7.");
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
        System.out.print("Matricula: ");
        String matricula = scanner.nextLine().trim();

        // Validação de campo vazio
        if (matricula.isEmpty()) {
            System.out.println("Erro: A matricula nao pode ser vazia.");
            return;
        }

        // Validação de matrícula única
        if (buscarPorMatricula(matricula) != null) {
            System.out.println("Ja existe ficha com a matricula " + matricula + "!");
            return;
        }

        System.out.print("Nome: ");
        String nome = scanner.nextLine().trim();
        if (nome.isEmpty()) {
            System.out.println("Erro: O nome nao pode ser vazio.");
            return;
        }

        System.out.print("Curso: ");
        String curso = scanner.nextLine().trim();

        System.out.print("Cidade: ");
        String cidade = scanner.nextLine().trim();

        listaAlunos.add(new Aluno(matricula, nome, curso, cidade));
        System.out.println("Ficha de " + nome + " arquivada!");
    }

    private static void listarAlunos() {
        if (listaAlunos.isEmpty()) {
            System.out.println("Nenhuma ficha no gaveteiro.");
            return;
        }
        System.out.println("\n--- FICHAS NO GAVETEIRO: " + listaAlunos.size() + " ---");
        for (Aluno a : listaAlunos) {
            System.out.println(a); // Chama o toString() da classe Aluno
        }
    }

    private static void buscarEExibirAluno() {
        System.out.print("Matricula procurada: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
        } else {
            System.out.println("Achei: " + a);
        }
    }

    private static void atualizarAluno() {
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }

        System.out.print("Novo curso de " + a.getNome() + ": ");
        String novoCurso = scanner.nextLine();
        if (!novoCurso.isEmpty()) {
            a.setCurso(novoCurso); // Altera o objeto original
        }

        System.out.println("Ficha atualizada: " + a);
    }

    private static void removerAluno() {
        System.out.print("Matricula da ficha a remover: ");
        String matricula = scanner.nextLine();
        Aluno a = buscarPorMatricula(matricula);

        if (a == null) {
            System.out.println("Nenhuma ficha com a matricula " + matricula + ".");
            return;
        }

        System.out.print("Tem certeza que remove " + a.getNome() + "? (s/n): ");
        String confirmacao = scanner.nextLine();

        if (confirmacao.equalsIgnoreCase("s")) {
            listaAlunos.remove(a);
            System.out.println("Ficha removida.");
        } else {
            System.out.println("Remocao cancelada.");
        }
    }

    private static void gerarRelatorio() {
        System.out.println("\n--- RELATORIO DA SECRETARIA ---");
        System.out.println("Total de fichas: " + listaAlunos.size());

        System.out.print("Contar alunos de qual curso? ");
        String cursoProcurado = scanner.nextLine().trim();

        // preparar (ANTES do for)
        int contador = 0;

        // percorrer
        for (Aluno a : listaAlunos) {
            if (a.getCurso().equalsIgnoreCase(cursoProcurado)) {
                contador++;
            }
        }

        // usar
        System.out.println("Alunos de " + cursoProcurado + ": " + contador);
    }

    // MELHORIA (a): Buscar aluno por Nome
    private static void buscarPorNomeExibir() {
        System.out.print("Nome procurado: ");
        String nomeProcurado = scanner.nextLine().trim();
        boolean encontrado = false;

        for (Aluno a : listaAlunos) {
            if (a.getNome().equalsIgnoreCase(nomeProcurado)) {
                System.out.println("Achei: " + a);
                encontrado = true;
            }
        }

        if (!encontrado) {
            System.out.println("Nenhuma ficha encontrada para o nome: " + nomeProcurado);
        }
    }
}