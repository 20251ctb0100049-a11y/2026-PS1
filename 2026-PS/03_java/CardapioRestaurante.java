import java.util.Random;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random random = new Random(); 

        double valorTotal = 0;
        String resumoPedido = "";
        int continuar = 1;

        while (continuar == 1) {

            System.out.println("=================================");
            System.out.println("       Restaurante FMS");
            System.out.println("     CARDÁPIO ELETRÔNICO");
            System.out.println("=================================");
            System.out.println("1 - X-Burguer .......... R$ 18,00");
            System.out.println("2 - Pizza .............. R$ 35,00");
            System.out.println("3 - Batata Frita ....... R$ 12,00"); 
            System.out.println("4 - Refrigerante ....... R$ 8,00");  
            System.out.println("5 - Sorvete ............ R$ 10,00");
            System.out.println("6 - Sair do cardápio (Fechar)"); 
            System.out.println("=================================");

            System.out.print("Escolha uma opção: ");
            int opcao = entrada.nextInt();

            // Se escolher 6, exibe a mensagem, fecha o scanner e encerra o programa na hora
            if (opcao == 6) {
                System.out.println("\nPedido cancelado. Volte sempre!.");
                entrada.close();
                return; // Fecha o programa imediatamente
            }

            String produto = "";
            double preco = 0;

            if (opcao == 1) {
                produto = "X-Burguer";
                preco = 18.00;
            } else if (opcao == 2) {
                produto = "Pizza";
                preco = 35.00;
            } else if (opcao == 3) {
                produto = "Batata Frita";
                preco = 12.00;
            } else if (opcao == 4) {
                produto = "Refrigerante";
                preco = 8.00;
            } else if (opcao == 5) {
                produto = "Sorvete";
                preco = 10.00;
            } else {
                System.out.println("Opção indisponivel no momento.");
                continue;
            }

            System.out.println("Você escolheu " + produto);
            System.out.println("Valor unitário: R$" + preco);
            System.out.print("Quantidade: ");
            int quantidade = entrada.nextInt();

            double subtotal = preco * quantidade;
            valorTotal = valorTotal + subtotal; 
            resumoPedido = resumoPedido + quantidade + "x " + produto + " ..... R$ " + subtotal + "\n"; 

            System.out.println("Item adicionado ao pedido!");

            System.out.println("\nDeseja continuar comprando?");
            System.out.println("1 - Sim (Voltar ao Cardápio)");
            System.out.println("2 - Finalizar e ir para o Pagamento");
            System.out.print("Escolha: ");
            continuar = entrada.nextInt();
        }

        // Esta parte só será executada se o usuário terminar de comprar e escolher "2 - Finalizar"
        System.out.println("\n===========================");
        System.out.println("     RESUMO DO PEDIDO      ");
        System.out.println("===========================");
        System.out.print(resumoPedido);
        System.out.println("\nTOTAL: R$ " + valorTotal);
        System.out.println("===========================");

        System.out.println("\nForma de pagamento:");
        System.out.println("1 - Dinheiro");
        System.out.println("2 - Cartão");
        System.out.println("3 - PIX");
        System.out.print("Escolha: ");
        int pagamento = entrada.nextInt();

        System.out.println("\nPagamento realizado com sucesso!");

        int numeroPedido = random.nextInt(500) + 1;

        System.out.println("Pedido Nº " + numeroPedido);
        System.out.println("Aguarde a chamada do seu pedido.");

        entrada.close();
    }
}