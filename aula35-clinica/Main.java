import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Produto> produtos = new ArrayList<>();

    public static void main(String[] args) {

        int opcao = 0;

        while (opcao != 5) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preço");
            System.out.println("4 - Remover");
            System.out.println("5 - Sair");
            System.out.print("Opção: ");

            opcao = teclado.nextInt();
            teclado.nextLine();

            if (opcao == 1) {
                cadastrar();
            } else if (opcao == 2) {
                listar();
            } else if (opcao == 3) {
                alterarPreco();
            } else if (opcao == 4) {
                remover();
            }
        }

        System.out.println("Sistema encerrado.");
    }

    // Método de busca corrigido
    static Produto buscarPorCodigo(int codigo) {
        for (Produto p : produtos) {
            if (p.getCodigo() == codigo) { 
                return p;
            }
        }
        return null;
    }

    static void cadastrar() {
        System.out.print("Código: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();

        if (buscarPorCodigo(codigo) != null) {
            System.out.println("Erro: Código já cadastrado!");
            return;
        }

        System.out.print("Nome: ");
        String nome = teclado.nextLine();

        System.out.print("Preço: ");
        double preco = teclado.nextDouble();
        teclado.nextLine();

        Produto p = new Produto(codigo, nome, preco);
        produtos.add(p);
        System.out.println("Produto cadastrado com sucesso!");
    }

    static void listar() {
        if (produtos.isEmpty()) {
            System.out.println("Nenhum produto cadastrado.");
            return;
        }

        for (Produto p : produtos) {
            System.out.println(p);
        }
    }

    static void alterarPreco() {
        System.out.print("Código do produto: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();

        Produto p = buscarPorCodigo(codigo);

        if (p == null) {
            System.out.println("Produto não encontrado!");
            return;
        }

        System.out.print("Novo preço: ");
        double preco = teclado.nextDouble();
        teclado.nextLine();

        System.out.print("Tem desconto? (1-Sim / 2-Não): ");
        int temDesconto = teclado.nextInt();
        teclado.nextLine();

        if (temDesconto == 1) {
            System.out.print("Porcentagem de desconto (%): ");
            double desconto = teclado.nextDouble();
            teclado.nextLine();
            p.alterarPreco(preco, desconto);
        } else {
            p.alterarPreco(preco);
        }

        System.out.println("Preço atualizado!");
    }

    static void remover() {
        System.out.print("Código do produto a remover: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();

        Produto p = buscarPorCodigo(codigo);

        if (p == null) {
            System.out.println("Produto não encontrado!");
            return;
        }

        produtos.remove(p);
        System.out.println("Produto removido com sucesso!");
    }
}