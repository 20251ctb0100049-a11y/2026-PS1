public class TesteValidadorLivro {

    public static void main(String[] args) {

        testar("", "Machado de Assis", 1899);

        testar("Dom Casmurro", "", 1899);

        testar("Dom Casmurro", "Machado de Assis", -10);

        testar("Dom Casmurro", "Machado de Assis", 1899);
    }

    private static void testar(
            String titulo,
            String autor,
            int ano) {

        try {
            ValidadorLivro.validar(titulo, autor, ano);
            System.out.println("Livro válido: " + titulo);

        } catch (LivroInvalidoException e) {
            System.out.println("Livro inválido: " + e.getMessage());
        }
    }
}