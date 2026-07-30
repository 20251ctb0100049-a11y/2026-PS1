package rafael;
public class Produto {
    private String nome;
    private double preco;
    private int quantidade;

    public Produto(String nome, double preco, int quantidade) {
        setNome(nome);
        setPreco(preco);
        setQuantidade(quantidade);
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setNome(String nome) {
        if (nome != null && !nome.isBlank()) {
            this.nome = nome;
        }
    }

    public void setPreco(double preco) {
        if (preco >= 0) {
            this.preco = preco;
        }
    }

    public void setQuantidade(int quantidade) {
        if (quantidade >= 0) {
            this.quantidade = quantidade;
        }
    }

    public void adicionarEstoque(int quantidadeAdicionar) {
        if (quantidadeAdicionar > 0) {
            quantidade += quantidadeAdicionar;
        }
    }

    public boolean removerEstoque(int quantidadeRemover) {
        if (quantidadeRemover > 0 && quantidadeRemover <= quantidade) {
            quantidade -= quantidadeRemover;
            return true;
        }
        return false;
    }

    public double calcularValorEmEstoque() {
        return preco * quantidade;
    }
}