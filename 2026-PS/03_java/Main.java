import rafael.Produto;

public class Main {
    public static void main(String[] args) {
        Produto produto = new Produto("Mouse", 80.00, 10);

        produto.adicionarEstoque(5);
        boolean removido = produto.removerEstoque(3);

        System.out.println("Produto: " + produto.getNome());
        System.out.println("Preço: R$ " + produto.getPreco());
        System.out.println("Quantidade: " + produto.getQuantidade());
        System.out.println("Remoção realizada: " + removido);
        System.out.println("Valor em estoque: R$ "
                + produto.calcularValorEmEstoque());
    }
}
