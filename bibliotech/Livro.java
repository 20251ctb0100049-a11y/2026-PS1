public class Livro {

    private int id;
    private String titulo;
    private String autor;
    private int ano;

    // Construtor sem ID (para novos cadastros antes de salvar no banco)
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }

    // Construtor completo com ID (para registros vindos do MariaDB)
    public Livro(int id, String titulo, String autor, int ano) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }

    // Getters e Setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }
}