import java.util.List;

public class TesteListarLivros {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();
        List<Livro> livros = dao.listarLivros();

        System.out.println("=== LIVROS CADASTRADOS ===");

        if (livros.isEmpty()) {
            System.out.println("Nenhum livro encontrado.");
        } else {
            for (Livro livro : livros) {
                System.out.println(
                    livro.getId() + " - " +
                    livro.getTitulo() + " - " +
                    livro.getAutor() + " (" +
                    livro.getAno() + ")"
                );
            }

            // --- Desafio Prático: Filtrar no Java (Ano >= 2000) ---
            System.out.println("\n=== LIVROS PUBLICADOS A PARTIR DE 2000 (Filtro Java) ===");
            for (Livro livro : livros) {
                if (livro.getAno() >= 2000) {
                    System.out.println(
                        livro.getTitulo() + " (" + livro.getAno() + ")"
                    );
                }
            }
        }
    }
}