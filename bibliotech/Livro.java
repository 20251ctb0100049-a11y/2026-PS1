/*
 * Disciplina: 2026-PS
 * Projeto    : bibliotech
 * Arquivo    : Livro.java
 * Autor      : seu nome
 * Descricao  : a caixa "Livro" do diagrama de classes, em Java (Aula 37).
 */
public class Livro {

    // ATRIBUTOS: a faixa do meio da caixa, um por linha, todos private.
    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;

    // CONSTRUTOR 1: com 3 parâmetros (titulo, autor e ano)
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true; 
    }

    // CONSTRUTOR 2 (ADICIONADO): aceita apenas 2 parâmetros e atribui ano padrão 0
    public Livro(String titulo, String autor) {
        this(titulo, autor, 0);
    }

    // GETTERS: as janelas de leitura.
    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
    }

    // OPERACAO DA CAIXA: estaDisponivel(), a faixa de baixo do diagrama.
    public boolean estaDisponivel() {
        return disponivel;
    }

    // Os dois metodos que o emprestimo vai usar na Aula 38.
    public void emprestar() {
        this.disponivel = false;
    }

    public void devolver() {
        this.disponivel = true;
    }

    // toString: como a ficha se apresenta (Aula 34).
    public String toString() {
        String situacao = disponivel ? "disponivel" : "emprestado";
        return titulo + " (" + autor + ", " + ano + ") - " + situacao;
    }

}