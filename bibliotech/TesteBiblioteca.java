public class TesteBiblioteca {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(new Livro("Dom Casmurro", "Machado de Assis", 1899));
        biblioteca.cadastrarLivro(new Livro("Capitaes da Areia", "Jorge Amado", 1937));
        
        biblioteca.cadastrarLeitor(new Leitor("Pedro Alves", "2026010", 1));
        biblioteca.cadastrarLeitor(new Leitor("Ana Lima", "2026011", 2));

        biblioteca.emprestar("Dom Casmurro", "2026010");

        // Testes de Devolução
        System.out.println("Devolucao: " + biblioteca.devolver("Dom Casmurro"));
        System.out.println("Segunda devolucao: " + biblioteca.devolver("Dom Casmurro"));

        System.out.println("Ana pega Dom Casmurro: " + biblioteca.emprestar("Dom Casmurro", "2026011"));

        System.out.println("--- Emprestimos ---");
        biblioteca.listarEmprestimos();

        System.out.println("--- Acervo ---");
        biblioteca.listarAcervo();
    }
}